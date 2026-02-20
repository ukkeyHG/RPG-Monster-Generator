import random
import re
from rpg_character_data.rpg_monster_species_data import MONSTER_SPECIES_DATA
from rpg_character_data.rpg_monster_element_data import MONSTER_ELEMENT_DATA
from rpg_character_data.rpg_monster_variant_data import MONSTER_VARIANT_DATA
from rpg_character_data.rpg_monster_rank_data import MONSTER_RANK_DATA
from rpg_character_data.rpg_scene_data import SCENE_DATA


# スタイルは文末に配置するように変更
# Echoes of Eltnia 標準の重厚な油彩画スタイル
BASE_STYLE = (
    "Dark fantasy oil painting style, heavy painterly brushstrokes, moody chiaroscuro lighting. "
    "90s classic RPG illustration aesthetic, high contrast, gritty texture. "
    "NO UI, NO TEXT, NO BUTTONS. High detail, masterwork level"
)

def resolve_prompt_variants_with_trace(text):
    if not text: return "", []
    pattern = r"\{([^{}]+)\}"
    selections = []
    def replacer(match):
        choice = random.choice(match.group(1).split("|"))
        selections.append(choice)
        return choice
    return re.sub(pattern, replacer, text), selections

class RPGGenerator:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "species": (list(MONSTER_SPECIES_DATA.keys()),),
                "element": (list(MONSTER_ELEMENT_DATA.keys()),),
                "variant": (list(MONSTER_VARIANT_DATA.keys()),),
                "rank": (list(MONSTER_RANK_DATA.keys()),),
                "scene": (list(SCENE_DATA.keys()),),
            }
        }

    RETURN_TYPES = ("STRING", "STRING", "STRING", "STRING")
    RETURN_NAMES = ("positive_prompt", "negative_prompt", "Ollama_Generate_V2_Textbox_2", "selection_summary")
    FUNCTION = "generate_prompt"
    CATEGORY = "RPG"

    def generate_prompt(self, species, element, variant, rank, scene):
        # データの順序：種族を最優先(1番目)にする
        order = [
            MONSTER_SPECIES_DATA[species],
            MONSTER_ELEMENT_DATA[element],
            MONSTER_VARIANT_DATA[variant],
            MONSTER_RANK_DATA[rank],
            SCENE_DATA[scene]
        ]

        resolved_positives = []
        resolved_negatives = ["modern, sci-fi, anime, photo, humanoid, warrior, person, man, woman"]
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

        # 重要：種族プロンプトを先頭、画風スタイルを最後にする。結合には . (ピリオド) を使用。
        final_positive = ", ".join(filter(None, resolved_positives))
        final_positive = f"{final_positive}. {BASE_STYLE}"
        
        final_negative = ", ".join(filter(None, resolved_negatives))

        summary = f"Species: {species}\nElement: {element}\nVariant: {variant}\nRank: {rank}\nScene: {scene}"
        if all_selections: summary += "\nChoices: " + ", ".join(all_selections)

        return (final_positive, final_negative, final_positive, summary)

NODE_CLASS_MAPPINGS = {"RPG-Monster-Generator": RPGGenerator}
NODE_DISPLAY_NAME_MAPPINGS = {"RPG-Monster-Generator": "RPG Monster Generator"}

