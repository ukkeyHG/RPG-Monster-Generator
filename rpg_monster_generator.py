import random
import re
from nodes import CLIPTextEncode
from .rpg_character_data.rpg_monster_species_data import MONSTER_SPECIES_DATA
from .rpg_character_data.rpg_monster_element_data import MONSTER_ELEMENT_DATA
from .rpg_character_data.rpg_monster_variant_data import MONSTER_VARIANT_DATA
from .rpg_character_data.rpg_monster_rank_data import MONSTER_RANK_DATA
from .rpg_character_data.rpg_scene_data import SCENE_DATA


# 高品質なスタイルプリセット
STYLE_DATA = {
    "Oil Painting": {
        "positive": (
            "Dark fantasy oil painting style, heavy painterly brushstrokes, moody chiaroscuro lighting. "
            "90s classic RPG illustration aesthetic, high contrast, gritty texture. "
            "NO UI, NO TEXT, NO BUTTONS. High detail, masterwork level"
        ),
        "negative": "",
        "steps": 30,
        "cfg": 8.0,
        "sampler_name": "dpmpp_2m",
        "scheduler": "karras"
    },
    "Cinematic Realistic": {
        "positive": (
            "Cinematic dark fantasy photography, highly detailed monster textures, subsurface scattering, "
            "moody chiaroscuro lighting, volumetric fog, realistic skin, 8k UHD, RAW photo, "
            "hyperrealistic, extremely detailed. NO UI, NO TEXT"
        ),
        "negative": "painting, drawing, illustration, sketch",
        "steps": 35,
        "cfg": 6.5,
        "sampler_name": "dpmpp_3m_sde_gpu",
        "scheduler": "karras"
    },
    "Ancient Sketch": {
        "positive": (
            "Rough hand-drawn charcoal and graphite sketch, edge-to-edge drawing, loose pencil lines, messy graphite strokes, "
            "artistic study, cross-hatching, smudges, unfinished look, monochrome, "
            "antique textured paper background, weathered edges. "
            "NO COLORS, NO DIGITAL, NO PHOTO, NO TEXT"
        ),
        "negative": "color, digital, photo, realistic, 3d, painting, render, smooth, frame, border, boxed, margins",
        "steps": 20,
        "cfg": 5.0,
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
            }
        }

    RETURN_TYPES = ("STRING", "STRING", "CONDITIONING", "CONDITIONING", "INT", "FLOAT", "COMBO", "COMBO")
    RETURN_NAMES = (
        "positive_prompt", 
        "negative_prompt", 
        "positive_conditioning", 
        "negative_conditioning",
        "steps",
        "cfg",
        "sampler_name",
        "scheduler"
    )
    FUNCTION = "generate_prompt"
    CATEGORY = "RPG"

    def generate_prompt(self, clip, style, species, element, variant, rank, scene):
        # データの順序：種族を最優先(1番目)にする
        order = [
            MONSTER_SPECIES_DATA[species],
            MONSTER_ELEMENT_DATA[element],
            MONSTER_VARIANT_DATA[variant],
            MONSTER_RANK_DATA[rank],
            SCENE_DATA[scene]
        ]

        resolved_positives = []
        # 基本的なネガティブセットに枠線抑制を追加
        resolved_negatives = [
            "modern, sci-fi, anime, photo, humanoid, warrior, person, man, woman, "
            "frame, border, boxed, picture frame, cropping, margins, bleed, canvas frame"
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
        base_style_prompt = style_config["positive"]
        style_negative = style_config["negative"]
        
        # KSampler 推奨値
        steps = style_config["steps"]
        cfg = style_config["cfg"]
        sampler_name = style_config["sampler_name"]
        scheduler = style_config["scheduler"]

        # 重要：種族プロンプトを先頭、画風スタイルを最後にする。結合には . (ピリオド) を使用。
        final_positive = ", ".join(filter(None, resolved_positives))
        final_positive = f"{final_positive}. {base_style_prompt}"
        
        # スタイル固有のネガティブがある場合は追加
        if style_negative:
            resolved_negatives.insert(0, style_negative)

        final_negative = ", ".join(filter(None, resolved_negatives))

        # Encode prompts
        encoder = CLIPTextEncode()
        encoded_positive = encoder.encode(clip, final_positive)[0]
        encoded_negative = encoder.encode(clip, final_negative)[0]

        return (
            final_positive, 
            final_negative, 
            encoded_positive, 
            encoded_negative,
            steps,
            cfg,
            sampler_name,
            scheduler
        )

NODE_CLASS_MAPPINGS = {"RPG-Monster-Generator": RPGMonsterGenerator}
NODE_DISPLAY_NAME_MAPPINGS = {"RPG-Monster-Generator": "RPG Monster Generator"}



