# rpg_monster_species_data.py

MONSTER_SPECIES_DATA = {
    "Slime": {
        "prompt": "A plump teardrop-shaped mound of translucent viscous slime, {peaked dome shape slumped on floor|partially melted and spreading|pointed mounded heap}, {broad bottom spreading on the stone floor|wide spreading puddle}, {swirling surface patterns|trapped debris|internal nucleus}, glistening wet texture, directly on the dungeon floor",
        "negative_prompt": "sphere, ball, orb, perfect circle, round object, symmetrical, floating, flying, suspended, air-borne, watery, thin liquid, pedestal, platform, humanoid, face, eyes, mouth, teeth, nose, head, limbs, arms, legs, hands, feet, claws, wings, tail, muscular, clothes, text, watermark"
    },
    "Skeleton": {
        "prompt": "An animated skeletal warrior, {front view|three-quarter view|side profile}, {advancing slowly|shield raised|crouched on one knee|standing tall|lunging forward with weapon|aiming from a side stance}, {rusted iron breastplate|shredded battle-torn banner|ancient necklaces of bone|shattered legionnaire armor|broken ribs exposed}, {wielding a rusty longsword and a cracked wooden shield|aiming a bone bow with both hands|brandishing a jagged iron spear|wielding a heavy iron mace and a battered buckler|bare bony hands}, bleached bones, glowing hollow eye sockets",
        "negative_prompt": "flesh, skin, muscle, fat, hair, living person, static pose"
    },
    "Orc": {
        "prompt": "A brutal muscular orc warrior with tusks, {front view|three-quarter view|side profile}, {roaring and lunging|heavy breathing stance|brandishing weapon|imposing warrior walk|bracing for impact in a low crouch}, {massive notched axe|heavy spiked club|dual-wielding cleavers|hand-and-a-half sword}, {crude tribal tattoos|fur-lined shoulder pad|heavy studded leather belt|bone trophies hanging from belt|furred mantle|scars across chest}, battle-scarred skin, heavy build",
        "negative_prompt": "animal, weak, thin, friendly gaze, static pose"
    },
    "Dragon": {
        "prompt": "A colossal ancient dragon with massive leathery wings, {diving from the sky|soaring with speed|three-quarter ground stance}, {jagged reptilian scales|ancient battle scars|glowing chest preparing breath}, imposing and powerful presence",
        "negative_prompt": "humanoid, person, human, clothes, standing on two legs, arms, warrior, static pose"
    },
    "Bat": {
        "prompt": "A {giant leathery-winged cave bat|swarm of small bats merging}, {clinging to ceiling upside down|screeching with wings spread|flying through dark mist}, sharp fangs, furred body",
        "negative_prompt": "humanoid, person, legs, standing, bird, static pose"
    },
    "Rat": {
        "prompt": "A mutated {giant rat beast|pack of scurrying rats}, {hiding in shadows|gnawing on bones|scuttling on dungeon floor}, mangy fur, glowing red eyes, sharp claws",
        "negative_prompt": "humanoid, person, standing, cute, pet, static pose"
    },
    "Frog": {
        "prompt": "A bloated toad-like monster, {preparing to leap|tongue lashed out|crouched on a mossy stone}, warty necrotic skin, predatory yellow eyes",
        "negative_prompt": "humanoid, person, clothes, cute, small frog, static pose"
    },
    "Spider": {
        "prompt": "A massive venomous giant spider, {skittering on web|descending from silk thread|ambushing from shadows}, multiple glowing eyes, hairy chitinous legs",
        "negative_prompt": "humanoid, person, face, two legs, arms, static pose"
    },
    "Kobold": {
        "prompt": "A small reptilian kobold warrior, {scouting with a flickering torch|hiding behind dungeon debris|brandishing a crude spear}, animalistic features, lizard-like skin",
        "negative_prompt": "human, beautiful, tall, static pose"
    },
    "Goblin": {
        "prompt": "A small malevolent green-skinned goblin, {front view|three-quarter view|side profile}, {sneaking with a jagged dagger|cackling while pointing|skulking in dungeon shadows|clutching a stolen gemstone|aiming a poisoned shortbow|swinging a stolen mace|looking up and cackling}, pointed ears, snarling with sharp teeth",
        "negative_prompt": "human, beautiful, tall, static pose, barrel, box"
    },
    "Ogre": {
        "prompt": "A massive muscular ogre brute, {roaring and lunging|club raised high|imposing predatory walk}, thick hide, intimidating size, single horn",
        "negative_prompt": "humanoid, person, weak, small, static pose"
    },
    "Vampire": {
        "prompt": "A dark vampire lord, {wrapped in a voluminous dark cape|seated on a gothic throne|hovering above the floor}, pale skin, piercing red eyes, refined aristocratic attire",
        "negative_prompt": "animal, beast, sunlight, tan skin, human, static pose"
    },
    "Demon": {
        "prompt": "An infernal demon warrior, {three-quarter view|side profile|dynamic action pose}, {menacing crouch|spreading wings|clenched fists}, {jagged horns|curled demonic horns}, {tattered dark cape|clashing iron chains}, glowing eyes, surrounding hellfire aura",
        "negative_prompt": "angel, holy, human, person, simple front view, static pose, mugshot style"
    },
    "Ghost": {
        "prompt": "A translucent ethereal ghost apparition, {whispering and reaching out|passing through stone walls|flowing wispy form}, glowing mist, floating",
        "negative_prompt": "solid, physical, flesh, bone, humanoid, person, static pose"
    },
    "Hydra": {
        "prompt": "A multi-headed hydra beast, {multiple necks snapping and hissing|all heads facing different directions|coiled serpentine body}, dripping venom, reptilian scales",
        "negative_prompt": "humanoid, person, arms, legs, static pose"
    },
    "Manticore": {
        "prompt": "A winged manticore predator, {leaping with claws extended|soaring with bat wings|scorpion tail poised to strike}, lion body",
        "negative_prompt": "humanoid, person, static pose"
    },
    "Medusa": {
        "prompt": "(A full body study of a hybrid monster:1.3) in a (dynamic s-curve pose:1.1), (beautiful young woman's face with an alluring and seductive gaze:1.2), (natural human skin texture:1.1), (bewitching and powerful gorgon beauty:1.1) with writhing snakes for hair, {chest area completely protected by elegant form-fitting bronze and leather plating:1.3}, (sensual serpentine body with reptilian scales coiled on floor:1.2), petrifying gaze, wearing stone armor and mystical layered silk wraps, ominous and captivating presence",
        "negative_prompt": "animal, beast, bird head, snake head, mask, face plate, metallic face, porcelain skin, stiff face, plastic texture, closeup, portrait, headshot, cute, nudity, bare skin, exposed chest, nipples, (topless, naked breasts:1.5), man, male, warrior, weak, fragile, static pose"
    },
    "Gargoyle": {
        "prompt": "A stone-skinned winged gargoyle sentinel, {perched on a gothic pedestal|frozen in statue pose|spreading stony wings}, rocky texture",
        "negative_prompt": "flesh, skin, soft, flexible, human, humanoid, person, active movement"
    },
    "Lich": {
        "prompt": "An ancient skeletal lich necromancer, {casting a dark spell|levitating above bone pile|clutching an ancient grimoire}, tattered decayed cloth",
        "negative_prompt": "living, healthy skin, youthful, human, static pose"
    },
    "Mimic": {
        "prompt": "A living mimic chest monster, {lid wide open with sharp teeth|disguised as a common wooden chest|sticky tongue lashing out}, wooden texture",
        "negative_prompt": "humanoid, person, legs, arms, static pose"
    },
    "Wolf": {
        "prompt": "A savage giant wolf, {howling to the moon|leaping in attack|low predatory prowl}, bristling fur, snarling teeth",
        "negative_prompt": "humanoid, person, dog, domestic, static pose"
    },
    "Ghoul": {
        "prompt": "A feral gaunt undead creature, {hiding in a grave|feasting on remains|twitching erratic pose}, pale stretched skin, necrotic aura",
        "negative_prompt": "human, person, healthy, fat, static pose"
    },
    "Giant Worm": {
        "prompt": "A massive earthworm-like monster with a thick tubular fleshy body, {coiled into a dense spiral mound on the stone floor|spiraling into a circular pile}, pinkish-grey segmented skin, {glistening with slime|wet slimy texture}, circular mouth with rows of teeth, slithering in place",
        "negative_prompt": "humanoid, person, bird, legs, static pose, face only, wall, emerging from wall, thin body, skinny, stretched out, armored, robotic"
    },
    "Chimera": {
        "prompt": "A grotesque chimeric beast with {heads of a lion, goat, and snake|lion head roaring while snake tail strikes}, leathery bat wings, muscular body",
        "negative_prompt": "humanoid, person, small, cute, static pose"
    },
    "Flesh Golem": {
        "prompt": "A hulking construct of stitched muscle, {heavy shuffling gait|stitches pulling apart|electrified aura}, glowing necrotic energy",
        "negative_prompt": "human, natural, robotic, static pose"
    },
    "Harpy": {
        "prompt": "(A full body shot of a hybrid monster:1.3) in a (dynamic and seductive s-curve pose:1.2), (beautiful young woman's face with an alluring femme fatale gaze:1.2), (natural human skin texture:1.1), (bewitching yet elegant predator:1.1), {massive bird wings instead of arms|large wings attached to shoulders}, {chest and torso protected by elegant form-fitting silver armor plates and layered silk rags:1.3}, (lower body of a bird with powerful talons standing on ruins:1.2), seductive and ominous presence",
        "negative_prompt": "mask, face plate, metallic face, porcelain skin, stiff face, plastic texture, closeup, portrait, headshot, exposed breasts, nipples, bare skin, (topless, naked breasts:1.5), man, male, bird head, beak, avian face, animal face, bird torso, feathers on face, purely animal, cute, purely human, weak, fragile, static pose"
    },
    "Wraith": {
        "prompt": "A spectral figure, {fading in and out of shadows|raising a cold scythe|wispy trailing robes}, no face but glowing eyes, floating shadow",
        "negative_prompt": "solid, physical, flesh, bone, bright color, humanoid, person, static pose"
    },
    "Cerberus": {
        "prompt": "A massive monstrous hound with three distinct canine heads, {all heads snarling|guarding the gates of hell|full body visible in low stance}, powerful muscular build, thick black fur",
        "negative_prompt": "humanoid, person, cute, domestic dog, static pose, two heads, one head"
    },
}
