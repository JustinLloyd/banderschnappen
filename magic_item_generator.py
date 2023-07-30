import random


class MagicItemGenerator:
    pass

class MagicPotionGenerator:
    pass

class MinorMagicItemGenerator:
    pass

class MagicScrollGenerator:
    lesser_magic_items = [
        ('Potion of healing', 50, None),
        ('cantrip', 60, [
            'Spell scroll of Acid Splash',
            'Spell scroll of Chill Touch',
            'Spell scroll of Dancing Lights',
            'Spell scroll of Druidcraft',
            'Spell scroll of Eldritch Blast',
            'Spell scroll of Fire Bolt',
            'Spell scroll of Guidance',
            'Spell scroll of Mending',
            'Spell scroll of Message',
            'Spell scroll of Minor Illusion',
            'Spell scroll of Poison Spray',
            'Spell scroll of Produce Flame',
            'Spell scroll of Resistance',
            'Spell scroll of Sacred Flame',
            'Spell scroll of Shillelagh',
            'Spell scroll of Shocking Grasp',
            'Spell scroll of Spare the Dying',
            'Spell scroll of Thaumaturgy',
            'Spell scroll of True Strike',
            'Spell scroll of Vicious Mockery',
            'Spell scroll of Light',
            'Spell scroll of Mage Hand',
            'Spell scroll of Prestidigitation',
            'Spell scroll of Ray of Frost',
            # Add more cantrip spells as needed
        ]),
        ('Potion of climbing', 70, None),
        ('1st level spell scroll', 90, [
            'Spell scroll of Alarm',
            'Spell scroll of Animal Friendship',
            'Spell scroll of Bane',
            'Spell scroll of Bless',
            'Spell scroll of Burning Hands',
            'Spell scroll of Charm Person',
            'Spell scroll of Color Spray',
            'Spell scroll of Command',
            'Spell scroll of Comprehend Languages',
            'Spell scroll of Create or Destroy Water',
            'Spell scroll of Cure Wounds',
            'Spell scroll of Detect Evil and Good',
            'Spell scroll of Detect Magic',
            'Spell scroll of Detect Poison and Disease',
            'Spell scroll of Disguise Self',
            'Spell scroll of Divine Favor',
            'Spell scroll of Entangle',
            'Spell scroll of Expeditious Retreat',
            'Spell scroll of Faerie Fire',
            'Spell scroll of False Life',
            'Spell scroll of Feather Fall',
            'Spell scroll of Find Familiar',
            'Spell scroll of Floating Disk',
            'Spell scroll of Fog Cloud',
            'Spell scroll of Goodberry',
            'Spell scroll of Grease',
            'Spell scroll of Guiding Bolt',
            'Spell scroll of Healing Word',
            'Spell scroll of Hellish Rebuke',
            'Spell scroll of Heroism',
            'Spell scroll of Hideous Laughter',
            'Spell scroll of Hunter\'s Mark',
            'Spell scroll of Identify',
            'Spell scroll of Illusory Script',
            'Spell scroll of Inflict Wounds',
            'Spell scroll of Jump',
            'Spell scroll of Longstrider',
            'Spell scroll of Mage Armor',
            'Spell scroll of Magic Missile',
            'Spell scroll of Protection from Evil and Good',
            'Spell scroll of Purify Food and Drink',
            'Spell scroll of Sanctuary',
            'Spell scroll of Shield',
            'Spell scroll of Shield of Faith',
            'Spell scroll of Silent Image',
            'Spell scroll of Sleep',
            'Spell scroll of Speak with Animals',
            'Spell scroll of Thunderwave',
            'Spell scroll of Unseen Servant',
        ]),
        ('2nd level spell scroll', 94, [
            'Spell scroll of Acid Arrow',
            'Spell scroll of Aid',
            'Spell scroll of Alter Self',
            'Spell scroll of Animal Messenger',
            'Spell scroll of Arcane Lock',
            'Spell scroll of Arcanist\'s Magic Aurua',
            'Spell scroll of Augury',
            'Spell scroll of Barksin',
            'Spell scroll of Blindness/Deafness',
            'Spell scroll of Blur',
            'Spell scroll of Branding Smite',
            'Spell scroll of Calm Emotions',
            'Spell scroll of Continual Flame',
            'Spell scroll of Darkness',
            'Spell scroll of Darkvision',
            'Spell scroll of Detect Thoughts',
            'Spell scroll of Enhance Ability',
            'Spell scroll of Enlarge/Reduce',
            'Spell scroll of Enthrall',
            'Spell scroll of Find Steed',
            'Spell scroll of Find Traps',
            'Spell scroll of Flame Blade',
            'Spell scroll of Flaming Sphere',
            'Spell scroll of Gentle Repose',
            'Spell scroll of Gust of Wind',
            'Spell scroll of Heat Metal',
            'Spell scroll of Hold Person',
            'Spell scroll of Invisibility',
            'Spell scroll of Knock',
            'Spell scroll of Lesser Restoration',
            'Spell scroll of Levitate',
            'Spell scroll of Locate Animals or Plants',
            'Spell scroll of Locate Object',
            'Spell scroll of Magic Mouth',
            'Spell scroll of Magic Weapon',
            'Spell scroll of Mirror Image',
            'Spell scroll of Misty Step',
            'Spell scroll of Moonbeam',
            'Spell scroll of Pass Without Trace',
            'Spell scroll of Prayer of Healing',
            'Spell scroll of Protection from Poison',
            'Spell scroll of Ray of Enfeeblement',
            'Spell scroll of Rope Trick',
            'Spell scroll of Scorching Ray',
            'Spell scroll of See Invisibility',
            'Spell scroll of Shatter',
            'Spell scroll of Silence',
            'Spell scroll of Spider Climb',
            'Spell scroll of Spike Growth',
            'Spell scroll of Spiritual Weapon',
            'Spell scroll of Suggestion',
            'Spell scroll of Warding Bond',
            'Spell scroll of Web',
            'Spell scroll of Zone of Truth',

        ]),
        ('Potion of greater healing', 98, None),
        ('Bag of holding', 99, None),
        ('Driftglobe', 100, None)
    ]

    """
    01–15 	Potion of greater healing
16–22 	Potion of fire breath
23–29 	Potion of resistance
30–34 	Ammunition, +1
35–39 	Potion of animal friendship
40–44 	Potion of hill giant strength
45–49 	Potion of growth
50–54 	Potion of water breathing
55–59 	Spell scroll (2nd level)
60–64 	Spell scroll (3rd level)
65–67 	Bag of holding
68–70 	Keoghtom's ointment
71–73 	Oil of slipperiness
74–75 	Dust of disappearance
76–77 	Dust of dryness
78–79 	Dust of sneezing and choking
80–81 	Elemental gem
82–83 	Philter of love
84 	Alchemy jug
85 	Cap of water breathing
86 	Cloak of the manta ray
87 	Driftglobe
88 	Goggles of night
89 	Helm of comprehending languages
90 	Immovable rod
91 	Lantern of revealing
92 	Mariner's armor
93 	Mithral armor
94 	Potion of poison
95 	Ring of swimming
96 	Robe of useful items
97 	Rope of climbing
98 	Saddle of the cavalier
99 	Wand of magic detection
100 	Wand of secrets
    """

    @staticmethod
    def generate_lesser_magic_item():
        roll = random.randint(1, 100)

        for item, max_roll, additional_data in MagicItemGenerator.lesser_magic_items:
            if roll <= max_roll:
                if additional_data:
                    return random.choice(additional_data)
                else:
                    return item

        return 'Potion of healing'
