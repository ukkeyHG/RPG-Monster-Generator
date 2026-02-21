import random
import re
from nodes import CLIPTextEncode
from .rpg_character_data.rpg_monster_species_data import MONSTER_SPECIES_DATA
from .rpg_character_data.rpg_monster_element_data import MONSTER_ELEMENT_DATA
from .rpg_character_data.rpg_monster_variant_data import MONSTER_VARIANT_DATA
from .rpg_character_data.rpg_monster_rank_data import MONSTER_RANK_DATA
from .rpg_character_data.rpg_scene_data import SCENE_DATA


# ComfyUI の KSampler から直接型定義を取得して型ミスマッチを回避する
try:
    import nodes
    # KSampler の入力型定義（リスト）をそのまま取得して「自分の出力型」として利用する
    _ks_input = nodes.KSampler.INPUT_TYPES()["required"]
    SAMPLER_TYPE = _ks_input["sampler_name"][0]
    SCHEDULER_TYPE = _ks_input["scheduler"][0]
except Exception as e:
    # 失敗した場合のフォールバック
    SAMPLER_TYPE = ["euler", "euler_ancestral", "heun", "dpm_2", "dpm_2_ancestral", "lms", "dpm_fast", "dpm_adaptive", "dpmpp_2s_ancestral", "dpmpp_sde", "dpmpp_sde_gpu", "dpmpp_2m", "dpmpp_2m_sde", "dpmpp_2m_sde_gpu", "ddpm", "lcm"]
    SCHEDULER_TYPE = ["normal", "karras", "exponential", "sgm_uniform", "simple", "ddim_uniform"]

# 高品質なスタイルプリセット
STYLE_DATA = {
    "Oil Painting": {
        "positive": (
            "Masterpiece dark fantasy oil painting, heavy impasto brushstrokes, realistic paint texture, "
            "moody chiaroscuro lighting, deep shadows, rich dramatic colors, "
            "90s classic high-fantasy RPG manual illustration aesthetic, "
            "extremely detailed, fine art, professional oil on canvas. NO UI, NO TEXT."
        ),
        "negative": "anime, digital, 3d, photo, futuristic, minimalist, bright colors, flat lighting, clean lines",
        "steps": 30,
        "cfg": 8.0,
        "sampler_name": "dpmpp_2m",
        "scheduler": "karras"
    },
    "Cinematic Realistic": {
        "positive": (
            "Cinematic dark fantasy photography, highly detailed monster textures, subsurface scattering, "
            "moody chiaroscuro lighting, volumetric fog, realistic skin, 8k UHD, RAW photo, "
            "hyperrealistic, extremely detailed. NO UI, NO TEXT."
        ),
        "negative": "anime, painting, drawing, illustration, sketch",
        "steps": 35,
        "cfg": 6.5,
        "sampler_name": "dpmpp_3m_sde_gpu",
        "scheduler": "karras"
    },
    "Ancient Sketch": {
        "positive": (
            "Full body shot, edge-to-edge anatomy study, complete monster form visible, "
            "Rough hand-drawn charcoal and graphite sketch, loose pencil lines, messy graphite strokes, "
            "cross-hatching, smudges, unfinished look, monochrome, "
            "antique textured paper background, weathered edges. "
            "NO COLORS, NO DIGITAL, NO PHOTO, NO TEXT."
        ),
        "negative": "color, digital, photo, realistic, 3d, painting, render, smooth, frame, border, boxed, margins",
        "steps": 20,
        "cfg": 7.0,
        "sampler_name": "euler",
        "scheduler": "normal"
    },
    "Anime Cel Shaded": {
        "positive": (
            "Stylized 2D anime style, clean lineart, flat cel shading, vibrant colors, "
            "vivid high-quality anime illustration, character design sheet aesthetic, crisp edges, "
            "bold colors, simple shading. NO 3D, NO REALISTIC, NO OIL PAINTING, NO TEXTURE, NO TEXT."
        ),
        "negative": (
            "realistic, 3d, photo, oil painting, sketch, messy lines, blurry, distorted, grainy, "
            "detailed texture, realistic skin, noise, canvas texture, heavy brushstrokes"
        ),
        "steps": 28,
        "cfg": 7.5,
        "sampler_name": "dpmpp_2m",
        "scheduler": "karras"
    },
    "Pixel Art": {
        "positive": (
            "Hand-crafted 16-bit pixel art, {4k colors|4096 colors palette}, "
            "chunky pixels, visible pixel grid, sharp jagged edges, individual pixels, "
            "retro game sprite aesthetic, flat color shading. NO ANTI-ALIASING, NO SMOOTHING."
        ),
        "negative": (
            "anti-aliasing, smoothing, blur, gradient, painterly, realistic, 3d, photo, "
            "high definition textures, soft shading, blurry, anime style illustration"
        ),
        "steps": 25,
        "cfg": 7.0,
        "sampler_name": "euler",
        "scheduler": "normal"
    }
}

def resolve_prompt_variants_with_trace(text):
    if not text: return "", []
    pattern = r"\{([^{}]+)\}"
    selections = []
    def replacer(match):
        choice = random.choice(match.group(1).split("|"))
        selections.append(choice)
        return choice
    return re.sub(pattern, replacer, text), selections

class RPGMonsterGenerator:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "clip": ("CLIP",),
                "style": (list(STYLE_DATA.keys()),),
                "species": (list(MONSTER_SPECIES_DATA.keys()),),
                "element": (list(MONSTER_ELEMENT_DATA.keys()),),
                "variant": (list(MONSTER_VARIANT_DATA.keys()),),
                "rank": (list(MONSTER_RANK_DATA.keys()),),
                "scene": (list(SCENE_DATA.keys()),),
                "steps_offset": ("INT", {"default": 0, "min": -20, "max": 20, "step": 1}),
                "cfg_offset": ("FLOAT", {"default": 0.0, "min": -5.0, "max": 5.0, "step": 0.1}),
            }
        }

    RETURN_TYPES = ("STRING", "STRING", "CONDITIONING", "CONDITIONING", "INT", "FLOAT", SAMPLER_TYPE, SCHEDULER_TYPE, "STRING")
    RETURN_NAMES = (
        "positive_text", 
        "negative_text", 
        "conditioning_positive", 
        "conditioning_negative",
        "steps",
        "cfg",
        "sampler_name",
        "scheduler",
        "filename_prefix"
    )
    FUNCTION = "generate_prompt"
    CATEGORY = "RPG"

    def generate_prompt(self, clip, style, species, element, variant, rank, scene, steps_offset, cfg_offset):
        # データの役割に応じた順序付け
        order = [
            MONSTER_SPECIES_DATA[species], # 本体
            MONSTER_ELEMENT_DATA[element], # 属性装飾
            MONSTER_VARIANT_DATA[variant], # 状態/ポーズ
            MONSTER_RANK_DATA[rank],       # 格付け/威圧感
            SCENE_DATA[scene]              # 背景舞台
        ]

        resolved_positives = []
        # 基本的なネガティブセット（枠線・文字・署名抑制）
        # woman を削除し、性別を種族プロンプトで制御できるようにする
        resolved_negatives = [
            "modern, sci-fi, photo, "
            "closeup, portrait, headshot, bust, macro, cropped face, "
            "pedestal, platform, table, desk, display stand, "
            "frame, border, boxed, picture frame, cropping, margins, bleed, canvas frame, "
            "text, watermark, signature, letters, artist name, logo, words, digits"
        ]
        all_selections = []

        for entry in order:
            p, n = ("", "")
            if isinstance(entry, dict):
                p, n = entry.get("prompt", ""), entry.get("negative_prompt", "")
            else:
                p = str(entry)
            
            if p:
                res, sel = resolve_prompt_variants_with_trace(p)
                resolved_positives.append(res)
                all_selections.extend(sel)
            if n:
                res_n, _ = resolve_prompt_variants_with_trace(n)
                resolved_negatives.append(res_n)

        # 選択されたスタイル設定を取得
        style_config = STYLE_DATA.get(style, STYLE_DATA["Oil Painting"])
        style_positive = style_config["positive"]
        style_negative = style_config["negative"]
        
        # KSampler 推奨値 + オフセット適用
        steps = max(1, style_config["steps"] + steps_offset)
        cfg = max(0.0, style_config["cfg"] + cfg_offset)
        sampler_name = style_config["sampler_name"]
        scheduler = style_config["scheduler"]

        # パラメータ設計の再構築：
        # 1. スタイル(画風)を最優先(先頭)にする
        # 2. 種族以下をカンマで結合
        # 3. 画風と内容をピリオドで区切る
        content_prompt = ", ".join(filter(None, resolved_positives))
        final_positive = f"{style_positive} {content_prompt}"
        
        # スタイル固有のネガティブがある場合は追加
        if style_negative:
            resolved_negatives.insert(0, style_negative)

        final_negative = ", ".join(filter(None, resolved_negatives))

        # Encode prompts
        encoder = CLIPTextEncode()
        encoded_positive = encoder.encode(clip, final_positive)[0]
        encoded_negative = encoder.encode(clip, final_negative)[0]

        prefix = f"{species}_{element}"

        return (
            final_positive, 
            final_negative, 
            encoded_positive, 
            encoded_negative,
            steps,
            cfg,
            sampler_name,
            scheduler,
            prefix
        )

NODE_CLASS_MAPPINGS = {"RPG-Monster-Generator": RPGMonsterGenerator}
NODE_DISPLAY_NAME_MAPPINGS = {"RPG-Monster-Generator": "RPG Monster Generator"}



