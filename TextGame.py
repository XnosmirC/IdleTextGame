import random
import time

base_user_stats = {'attack': 5, 'defense': 5, 'element': None, 'gold': 0}  # Added 'gold' to user stats
small_monster_elements = ['fire', 'ice', 'electric', 'earth', 'spirit', 'darkness', 'poison', 'rage', 'neutral']
small_monster_kills = 0  # Counter for small monster kills
gold_per_small_monster = 10  # Define how much gold the player earns for each small monster killed
medium_monster_elements = ['fire', 'ice', 'electric', 'earth', 'spirit', 'darkness', 'poison', 'rage', 'neutral']
medium_monster_kills = 0  # Counter for small monster kills
gold_per_medium_monster = 30  # Define how much gold the player earns for each small monster killed

small_monster_base_stats = {'attack': 2, 'defense': 2, 'swing_speed': 1}
medium_monster_base_stats = {'attack': 5, 'defense': 7, 'swing_speed': 1.5}

user_stats = {'points': 0, 'gold': 10, 'stats': base_user_stats.copy(), 'bosses_slain': 0, 'spells': {}, 'equipment': {}, 'health': 100, 'small_monsters_defeated': 0}
user_id = 'player1'
# Initialize user_stats and user_id
user_id = 'user'
user_stats = {user_id: {'gold': 0, 'stats': base_user_stats.copy(), 'bosses_slain': 0, 'spells': {}, 'equipment': {}, 'health': 100, 'small_monsters_defeated': 0, 'potion_inventory': []}}


def increment_monster_stats(monster_stats, increment):
    for stat in monster_stats:
        monster_stats[stat] += increment
    return monster_stats

small_monster_base_stats = increment_monster_stats(small_monster_base_stats, 1)

medium_monster_base_stats = increment_monster_stats(medium_monster_base_stats, 2)

def kill_small_monster():
    global small_monster_kills
    small_monster_spawn_chance = 0.75
    small_monster_kills += 1
    base_user_stats['gold'] += gold_per_small_monster
    print(f"A small monster has been killed! You earned {gold_per_small_monster} gold. Total gold: {base_user_stats['gold']}")
    check_boss_spawn()

def kill_medium_monster():
    global medium_monster_kills
    medium_monster_spawn_chance = 0.25
    medium_monster_kills += 1
    base_user_stats['gold'] += gold_per_medium_monster 
    print(f"A medium monster has been killed! You earned {gold_per_medium_monster} gold. Total gold: {base_user_stats['gold']}")
    check_boss_spawn()

def check_boss_spawn():
    global small_monster_kills, medium_monster_kills
    total_kills = small_monster_kills + medium_monster_kills
    if total_kills >= 25:
        small_monster_kills = 0 
        medium_monster_kills = 0
        spawn_boss()

def spawn_boss():
    print("A boss has spawned!")

def defeat_boss():
    bonus_gold = int(base_user_stats['gold'] * 0.75) 
    base_user_stats['gold'] += bonus_gold 
    new_gold_per_kill = base_user_stats['gold'] / (small_monster_kills + medium_monster_kills + 1) 
    print(f"You defeated a boss! You earned a 75% bonus of {bonus_gold} gold. Total gold: {base_user_stats['gold']}. Now, gold earned per kill: {new_gold_per_kill}")

def add_to_inventory(item):
    if len(user_stats[user_id]['inventory']) < 20:
        user_stats[user_id]['inventory'].append(item)
        print(f"You've added {item} to your inventory.")
    else:
        print("Your inventory is full.")

user_stats[user_id]['potion_inventory'] = []

def add_potion_to_inventory(potion):
    if len(user_stats[user_id]['potion_inventory']) < 20:
        user_stats[user_id]['potion_inventory'].append(potion)
        print(f"You've added {potion} to your potion inventory.")
    else:
        print("Your potion inventory is full.")


def check_boss_rewards(bosses_slain):
    bonus_gold = 0
    bonus_items = []

    if bosses_slain >= 50 and bosses_slain % 5 == 0:
        bonus_gold = bosses_slain * 20
        bonus_items = ['unique', 'unique']
    elif bosses_slain == 50:
        bonus_gold = 1000
        bonus_items = ['unique']
    elif bosses_slain == 35:
        bonus_gold = 750
        bonus_items = ['epic', 'epic']
    elif bosses_slain == 30:
        bonus_gold = 500
        bonus_items = ['epic']
    elif bosses_slain == 25:
        bonus_gold = 300
        bonus_items = ['legendary', 'legendary']
    elif bosses_slain == 20:
        bonus_gold = 250
        bonus_items = ['legendary']
    elif bosses_slain == 15:
        bonus_gold = 200
        bonus_items = ['legendary', 'legendary']
    elif bosses_slain == 10:
        bonus_gold = 150
        bonus_items = ['rare']
    elif bosses_slain == 5:
        bonus_gold = 100
        bonus_items = ['rare']

    if bonus_gold > 0 and bonus_items:
        user_stats[user_id]['gold'] += bonus_gold
        for item in bonus_items:
            add_to_inventory(item)
        print(f"You've slain {bosses_slain} bosses! You earned a bonus of {bonus_gold} gold and the following items: {', '.join(bonus_items)}. Total gold: {user_stats[user_id]['gold']}")


# Elements
elements = ['fire', 'ice', 'electric', 'earth', 'spirit', 'darkness', 'poison', 'rage', 'neutral']

dot_values = {
    'common': 1,
    'uncommon': 2,
    'rare': 3,
    'epic': 3,
    'legendary': 3,
    'unique': 3
}

rarity_multipliers = {
    'common': 1,
    'uncommon': 1.25,
    'rare': 1.75,
    'epic': 2.25,
    'legendary': 2.75,
    'unique': 3.5
}

shop_items = {
    'Health Potion': {},
    'Antidote': {},
    'Weakness to {element} potion': {},
    'Extra Weakness to {element} potion': {},
    'Advanced Weakness to {element} potion': {},
    'Supreme Weakness to {element} potion' : {},
    'Magic Potion': {},
    'Apple Dumpling': {},
    'Beef Stew': {},
    'Baked Potatoes': {},
    'Gold Honey': {},
    'Red Honey': {},
    'Green Honey': {},
    'Blue Honey': {},
    'White Honey': {},
    'Black Honey': {},
    'Yellow Honey': {},
    'Orange Honey': {},
    'Purple Honey': {},
    'Clear Honey': {},
    'Dragon\'s Breath Mead': {},
    'Spiced Wine': {},
    'Juniper\'s Brew': {},
    'Underdark Ale': {},
    'Iced Lager': {},
    'Pixie Cider': {},
    'Orcish Rotgut Ale': {},
    'Asgardian Punch': {},
    'Party Popper Champagne': {},
    'Red Jelly': {},
    'Green Jelly': {},
    'Blue Jelly': {},
    'White Jelly': {},
    'Black Jelly': {},
    'Yellow Jelly': {},
    'Orange Jelly': {},
    'Purple Jelly': {},
    'Clear Jelly': {},
    'Red Ambrosia': {},
    'Green Ambrosia': {},
    'Blue Ambrosia': {},
    'White Ambrosia': {},
    'Black Ambrosia': {},
    'Yellow Ambrosia': {},
    'Orange Ambrosia': {},
    'Purple Ambrosia': {},
    'Clear Ambrosia': {},
    'Helmet': {},
    'Cloak': {},
    'Robes': {},
    'Chest': {},
    'Paulders': {},
    'Sleeves': {},
    'Gauntlets': {},
    'Legs': {},
    'Boots': {},
    'Necklace': {},
    'Ring': {},
    'Broach': {},
    'Bracelet': {},
    'One Handed Sword': {},
    'Dual Blades': {},
    'Two Handed Sword': {},
    'Recurve Bow': {},
    'Compound Bow': {},
    'Crossbow': {},
    'Staff': {},
    'One Handed Axe': {},
    'Two Handed Heavy Axe': {},
    'Dual Axes': {},
    'One Handed Hammer': {},
    'Two Handed Hammer': {},
    'Dagger': {},
    'Dual Daggers': {},
}

item_name = {
    'Health Potion': {},
    'Antidote': {},
    'Weakness to {element} potion': {},
    'Extra Weakness to {element} potion': {},
    'Advanced Weakness to {element} potion': {},
    'Supreme Weakness to {element} potion' : {},
    'Magic Potion': {},
    'Apple Dumpling': {},
    'Beef Stew': {},
    'Baked Potatoes': {},
    'Gold Honey': {},
    'Red Honey': {},
    'Green Honey': {},
    'Blue Honey': {},
    'White Honey': {},
    'Black Honey': {},
    'Yellow Honey': {},
    'Orange Honey': {},
    'Purple Honey': {},
    'Clear Honey': {},
    'Dragon\'s Breath Mead': {},
    'Spiced Wine': {},
    'Juniper\'s Brew': {},
    'Underdark Ale': {},
    'Iced Lager': {},
    'Pixie Cider': {},
    'Orcish Rotgut Ale': {},
    'Asgardian Punch': {},
    'Party Popper Champagne': {},
    'Red Jelly': {},
    'Green Jelly': {},
    'Blue Jelly': {},
    'White Jelly': {},
    'Black Jelly': {},
    'Yellow Jelly': {},
    'Orange Jelly': {},
    'Purple Jelly': {},
    'Clear Jelly': {},
    'Red Ambrosia': {},
    'Green Ambrosia': {},
    'Blue Ambrosia': {},
    'White Ambrosia': {},
    'Black Ambrosia': {},
    'Yellow Ambrosia': {},
    'Orange Ambrosia': {},
    'Purple Ambrosia': {},
    'Clear Ambrosia': {},
    'Helmet': {},
    'Cloak': {},
    'Robes': {},
    'Chest': {},
    'Paulders': {},
    'Sleeves': {},
    'Gauntlets': {},
    'Legs': {},
    'Boots': {},
    'Necklace': {},
    'Ring': {},
    'Broach': {},
    'Bracelet': {},
    'One Handed Sword': {},
    'Dual Blades': {},
    'Two Handed Sword': {},
    'Recurve Bow': {},
    'Compound Bow': {},
    'Crossbow': {},
    'Staff': {},
    'One Handed Axe': {},
    'Two Handed Heavy Axe': {},
    'Dual Axes': {},
    'One Handed Hammer': {},
    'Two Handed Hammer': {},
    'Dagger': {},
    'Dual Daggers': {},
}

for key in item_name:
    if key in shop_items:
        pass

rarities = ['common', 'uncommon', 'rare', 'epic', 'legendary', 'unique']

# Materials and their properties
materials = {
    'Cloth': {'defense': (0, 4), 'can_be_enchanted': True, 'rarity': ('common', 'unique')},
    'Leather': {'defense': (3, 7), 'can_be_enchanted': True, 'rarity': ('common', 'rare')},
    'Chain Mail': {'defense': (3, 8), 'can_be_enchanted': False, 'rarity': ('common', 'rare')},
    'Bone': {'defense': (6, 10), 'can_be_enchanted': True, 'rarity': ('common', 'legendary')},
    'Bronze': {'defense': (8, 14), 'can_be_enchanted': True, 'rarity': ('common', 'rare')},
    'Iron': {'defense': (5, 13), 'can_be_enchanted': True, 'rarity': ('common', 'epic')},
    'Gold': {'defense': (8, 15), 'can_be_enchanted': True, 'rarity': ('common', 'epic')},
    'Silver': {'defense': (8, 15), 'can_be_enchanted': True, 'rarity': ('common', 'epic')},
    'Steel': {'defense': (9, 18), 'can_be_enchanted': False, 'rarity': ('common', 'legendary')},
    'Ebony': {'defense': (12, 20), 'can_be_enchanted': True, 'rarity': ('rare', 'unique')},
    'Platinum': {'defense': (13, 22), 'can_be_enchanted': True, 'rarity': ('epic', 'unique')},
    'Diamond': {'defense': (0, 0), 'can_be_enchanted': True, 'rarity': ('rare', 'unique')},
    'Emerald': {'defense': (0, 0), 'can_be_enchanted': True, 'rarity': ('rare', 'unique')},
    'Quartz': {'defense': (0, 0), 'can_be_enchanted': True, 'rarity': ('common', 'rare')},
    'Ruby': {'defense': (0, 0), 'can_be_enchanted': True, 'rarity': ('uncommon', 'unique')},
    'Sapphire': {'defense': (0, 0), 'can_be_enchanted': True, 'rarity': ('epic', 'unique')},
    'Dragon Bone': {'defense': (16, 25), 'can_be_enchanted': True, 'rarity': ('epic', 'unique')},
    'Mithril': {'defense': (30, 45), 'can_be_enchanted': True, 'rarity': ('unique', 'unique')}
}

items = ['Helmet', 'Cloak', 'Robes', 'Chest', 'Paulders', 'Sleeves', 'Gauntlets', 'Legs', 'Boots', 'Necklace', 'Ring', 'Broach', 'Bracelet']

shop_items = {item: {'base_price': 150, 'material': random.choice(list(materials.keys())), 'rarity': random.choice(rarities), 'element': random.choice(elements), 'max_enchantments': 2 if item in ['Cloth', 'Leather', 'Cloak', 'Robes', 'Broach', 'Bracelet'] else 1} for item in items}

weapon_enchantments = {
    'Absorb Health': {'extra_damage': -1},
    'Absorb Magic': {'magic_absorption': 10},
    'Banish': {'banish': True},
    'Fear': {'fear': True},
    'Fire Damage': {'extra_damage': 10, 'burn': True},
    'Ice Damage': {'extra_damage': 5, 'slow': 0.25},
    'Magic Damage': {'magic_damage': 10},
    'Paralyze': {'paralyze': True},
    'Electric Damage': {'extra_damage': 8, 'magic_damage': 4},
    'Soul Trap': {'soul_trap': True}
}

armor_enchantments = {
    'Fortify Archery': {'damage_bonus': 0.15},
    'Fortify Barter': {'better_prices': 0.10},
    'Fortify Healing Rate': {'health_regeneration': 1},
    'Fortify Health': {'extra_health': 0.15},
    'Fortify Armor': {'extra_armor': 8},
    'Fortify Magic': {'extra_magic': 10},
    'Fortify Magic Regen': {'magic_regeneration': 1},
    'Fortify One-Handed': {'damage_bonus': 10},
    'Fortify Two-Handed': {'damage_bonus': 15},
    'Fortify Unarmed': {'extra_damage': 25},
    'Resist Fire': {'fire_resistance': 0.15},
    'Resist Ice': {'ice_resistance': 0.15},
    'Resist Magic': {'magic_resistance': 0.50},
    'Resist Poison': {'poison_resistance': True},
    'Resist Electric': {'electric_resistance': 0.30}
}

for item in shop_items.values():
    if 'can_be_enchanted' in item and item['can_be_enchanted']:
        if 'weapon' in item['type']:
            item['enchantments'] = random.sample(weapon_enchantments.keys(), k=2)
        elif item['type'] in ['armor', 'jewelry']:
            item['enchantments'] = random.sample(armor_enchantments.keys(), k=2)

for item in shop_items.values():
    if item.get('can_be_enchanted', False):
        if 'weapon' in item['type']:
            item['enchantments'] = random.sample(weapon_enchantments.keys(), k=2)
        elif item['type'] in ['armor', 'jewelry']:
            item['enchantments'] = random.sample(armor_enchantments.keys(), k=2)

def buy(item_name):
    user_id = 'user'  # Replace with actual user id


    if item_name in shop_items:
        item_price = shop_items[item_name]['price']

        if user_stats[user_id]['gold'] >= item_price:
            user_stats[user_id]['gold'] -= item_price

            user_stats[user_id]['inventory'][item_name] = shop_items[item_name]

            print(f"You've bought {item_name} for {item_price} gold.")

            if item_name == 'Pixie Cider':
                print("lol")
            elif item_name == 'Asgardian Punch':
                print("For Valhalla!")

        else:
            print("Not enough gold to buy the item.")
    else:
        print(f"{item_name} is not available in the shop.")

def update_shop_items():
    for item in shop_items.values():
        item['material'] = random.choice(list(materials.keys()))
        item['rarity'] = random.choice(rarities)
        item['element'] = random.choice(elements)
        item['defense'] = random.randint(*materials[item['material']]['defense'])
        item['can_be_enchanted'] = materials[item['material']]['can_be_enchanted']
        item['price'] = item['base_price'] * rarity_multipliers[item['rarity']]

new_items = {
    'Health Potion': {'price': 10, 'effect': {'health_boost': 0.20}},
    'Antidote': {'price': 12, 'effect': {'negate_poison': True}},
    'Weakness to {element} potion': {'price': 15, 'effect': {'extra_damage': 15}},
    'Extra Weakness to {element} potion': {'price': 30, 'effect': {'extra_damage': 30}},
    'Advanced Weakness to {element} potion': {'price': 45, 'effect': {'extra_damage': 45}},
    'Supreme Weakness to {element} potion' : {'price': 150, 'effect': {'extra_damage': 150}},
    'Magic Potion': {'price': 10, 'effect': {'magic_boost': 0.20}},
    'Apple Dumpling': {'price': 5, 'effect': {'health_boost': 10, 'bow_damage_boost': 0.05}},
    'Beef Stew': {'price': 3, 'effect': {'health_boost': 8}},
    'Baked Potatoes': {'price': 1, 'effect': {'health_boost': 5}},
    'Gold Honey': {'price': 100, 'effect': {'health_boost': 50}},
    'Red Honey': {'price': 25, 'effect': {'rage_damage_boost': 10}},
    'Green Honey': {'price': 25, 'effect': {'earth_damage_boost': 10}},
    'Blue Honey': {'price': 25, 'effect': {'ice_damage_boost': 10}},
    'White Honey': {'price': 25, 'effect': {'spirit_damage_boost': 10}},
    'Black Honey': {'price': 25, 'effect': {'darkness_damage_boost': 10}},
    'Yellow Honey': {'price': 25, 'effect': {'electric_damage_boost': 10}},
    'Orange Honey': {'price': 25, 'effect': {'fire_damage_boost': 10}},
    'Purple Honey': {'price': 25, 'effect': {'poison_damage_boost': 10}},
    'Clear Honey': {'price': 25, 'effect': {'neutral_damage_boost': 15}},
    'Dragon\'s Breath Mead': {'price': 1500, 'effect': {'fire_damage_boost': 100}},
    'Spiced Wine': {'price': 1500, 'effect': {'neutral_damage_boost': 150}},
    'Juniper\'s Brew': {'price': 1500, 'effect': {'earth_damage_boost': 100}},
    'Underdark Ale': {'price': 1500, 'effect': {'darkness_damage_boost': 100}},
    'Iced Lager': {'price': 1500, 'effect': {'ice_damage_boost': 100}},
    'Pixie Cider': {'price': 2000, 'effect': {'rage_damage_boost': 150}},
    'Orcish Rotgut Ale': {'price': 1500, 'effect': {'poison_damage_boost': 100}},
    'Asgardian Punch': {'price': 2000, 'effect': {'spirit_damage_boost': 150}},
    'Party Popper Champagne': {'price': 1500, 'effect': {'electric_damage_boost': 100}},
    'Red Jelly': {'price': 100, 'effect': {'rage_damage_boost': 50}},
    'Green Jelly': {'price': 100, 'effect': {'earth_damage_boost': 50}},
    'Blue Jelly': {'price': 100, 'effect': {'ice_damage_boost': 50}},
    'White Jelly': {'price': 100, 'effect': {'spirit_damage_boost': 50}},
    'Black Jelly': {'price': 100, 'effect': {'darkness_damage_boost': 50}},
    'Yellow Jelly': {'price': 100, 'effect': {'electric_damage_boost': 50}},
    'Orange Jelly': {'price': 100, 'effect': {'fire_damage_boost': 50}},
    'Purple Jelly': {'price': 100, 'effect': {'poison_damage_boost': 50}},
    'Clear Jelly': {'price': 100, 'effect': {'neutral_damage_boost': 75}},
    'Red Ambrosia': {'price': 100, 'effect': {'rage_damage_boost': 100}},
    'Green Ambrosia': {'price': 100, 'effect': {'earth_damage_boost': 100}},
    'Blue Ambrosia': {'price': 100, 'effect': {'ice_damage_boost': 100}},
    'White Ambrosia': {'price': 100, 'effect': {'spirit_damage_boost': 100}},
    'Black Ambrosia': {'price': 100, 'effect': {'darkness_damage_boost': 100}},
    'Yellow Ambrosia': {'price': 100, 'effect': {'electric_damage_boost': 100}},
    'Orange Ambrosia': {'price': 100, 'effect': {'fire_damage_boost': 100}},
    'Purple Ambrosia': {'price': 100, 'effect': {'poison_damage_boost': 100}},
    'Clear Ambrosia': {'price': 100, 'effect': {'neutral_damage_boost': 175}}
}


shop_items.update(new_items)

def equip(item_name):
    user_id = 'player1'

    if item_name in user_stats[user_id]['equipment']:
        if item_name in ['Broach', 'Bracelet']:
            if any(armor in user_stats[user_id]['equipment'] for armor in ['Cloth', 'Leather', 'Cloak', 'Robes']):
                user_stats[user_id]['stats']['element'] = user_stats[user_id]['equipment'][item_name]['element']
                user_stats[user_id]['stats']['defense'] += user_stats[user_id]['equipment'][item_name].get('defense_bonus', 0)
                print(f"You've equipped {item_name} with {user_stats[user_id]['stats']['element']} element. Bonuses added to stats.")
            else:
                print(f"You can't equip {item_name} without wearing Cloth, Leather, Cloak, or Robes.")
        else:
            user_stats[user_id]['stats']['element'] = user_stats[user_id]['equipment'][item_name]['element']
            user_stats[user_id]['stats']['attack'] += user_stats[user_id]['equipment'][item_name].get('attack_bonus', 0)
            user_stats[user_id]['stats']['defense'] += user_stats[user_id]['equipment'][item_name].get('defense_bonus', 0)
            print(f"You've equipped {item_name} with {user_stats[user_id]['stats']['element']} element. Bonuses added to stats.")
    else:
        print(f"You don't have {item_name} in your equipment.")

weapon_stats = {
    'One Handed Sword': {'base_price': 150, 'swing_speed': 1, 'attacks_per_minute': 60, 'damage': 5},
    'Dual Blades': {'base_price': 200, 'swing_speed': 1.25, 'attacks_per_minute': 75, 'damage': 10},
    'Two Handed Sword': {'base_price': 250, 'swing_speed': 0.75, 'attacks_per_minute': 45, 'damage': 12},
    'Recurve Bow': {'base_price': 100, 'reload_speed': 0.50, 'attacks_per_minute': 30, 'damage': 3},
    'Compound Bow': {'base_price': 150, 'reload_speed': 0.50, 'attacks_per_minute': 30, 'damage': 4},
    'Crossbow': {'base_price': 300, 'speed': 0.25, 'attacks_per_minute': 15, 'damage': 12},
    'Staff': {'base_price': 200, 'magic_speed': 1, 'attacks_per_minute': 60, 'damage': 4},
    'One Handed Axe': {'base_price': 200, 'swing_speed': 0.75, 'attacks_per_minute': 45, 'damage': 6},
    'Two Handed Heavy Axe': {'base_price': 350, 'swing_speed': 0.25, 'attacks_per_minute': 15, 'damage': 15},
    'Dual Axes': {'base_price': 300, 'swing_speed': 1, 'attacks_per_minute': 60, 'damage': 12},
    'One Handed Hammer': {'base_price': 200, 'swing_speed': 0.75, 'attacks_per_minute': 45, 'damage': 7},
    'Two Handed Hammer': {'base_price': 350, 'swing_speed': 0.25, 'attacks_per_minute': 15, 'damage': 16},
    'Dagger': {'base_price': 100, 'swing_speed': 1.75, 'attacks_per_minute': 105, 'damage': 3},
    'Dual Daggers': {'base_price': 200, 'swing_speed': 1.5, 'attacks_per_minute': 90, 'damage': 5},
}

shop_items = {weapon: {**stats, 'rarity': random.choice(rarities), 'element': random.choice(elements)} for weapon, stats in weapon_stats.items()}

weapons = ['One Handed Sword', 'Dual Blades', 'Two Handed Sword', 'Recurve Bow', 'Compound Bow', 'Crossbow', 'Staff', 'One Handed Axe', 'Two Handed Heavy Axe', 'Dual Axes', 'One Handed Hammer', 'Two Handed Hammer', 'Dagger', 'Dual Daggers']
armor = ['Helmet', 'Cloak', 'Robes', 'Chest', 'Paulders', 'Sleeves', 'Gauntlets', 'Legs', 'Boots', 'Necklace', 'Ring', 'Broach', 'Bracelet']

def update_shop_items():
    weapon_count = 0
    armor_count = 0

    for item in shop_items:
        if item in weapons:
            weapon_count += 1
        elif item in armor:
            armor_count += 1

    while weapon_count < 3:
        weapon = random.choice(weapons)
        if weapon not in shop_items:
            shop_items[weapon] = {'base_price': 150, 'material': random.choice(list(materials.keys())), 'rarity': random.choice(rarities), 'element': random.choice(elements), 'max_enchantments': 1}
            weapon_count += 1

    while armor_count < 3:
        piece = random.choice(armor)
        if piece not in shop_items:
            shop_items[piece] = {'base_price': 150, 'material': random.choice(list(materials.keys())), 'rarity': random.choice(rarities), 'element': random.choice(elements), 'max_enchantments': 2 if piece in ['Cloth', 'Leather', 'Cloak', 'Robes', 'Broach', 'Bracelet'] else 1}
            armor_count += 1

    for item in shop_items.values():
        item['rarity'] = random.choice(rarities)
        item['element'] = random.choice(elements)
        item['price'] = item['base_price'] * rarity_multipliers[item['rarity']]

if item_name in shop_items:
    item_price = shop_items[item_name]['price']
    pass
for key in item_name:
    if key in shop_items:
        pass  

if item_name not in shop_items:
    print(f"{item_name} is not available in the shop. Check back later!")
elif user_stats[user_id]['gold'] < item_price:
    print("Not enough gold to buy the item.")
else:
    user_stats[user_id]['gold'] -= item_price
    price_multiplier += 0.1

if item_name not in shop_items:
    print(f"{item_name} is not available in the shop. Check back later!")
elif user_stats[user_id]['gold'] < item_price:
    print("Not enough gold to buy the item.")
else:
    user_stats[user_id]['gold'] -= item_price
    # Increment the price multiplier by 1%
    price_multiplier += 0.1

    update_rarity(user_stats[user_id]['bosses_slain'])

    user_stats[user_id]['equipment'][item_name] = shop_items[item_name]

    print(f"You've bought {item_name} for {item_price} gold. Would you like to equip it? (yes/no)")

user_stats = {'points': 0, 'gold': 0, 'stats': base_user_stats.copy(), 'bosses_slain': 0, 'spells': {}, 'equipment': {}, 'health': 100, 'small_monsters_defeated': 0}

if random.random() < small_monster_spawn_chance:
    small_monster_element = random.choice(small_monster_elements)
    print(f"A wild {small_monster_element.capitalize()} Small Monster has appeared!")

if random.random() < medium_monster_spawn_chance:
    medium_monster_element = random.choice(medium_monster_elements)
    print(f"A wild {medium_monster_element.capitalize()} medium Monster has appeared!")

def update_rarity(bosses_defeated):
    user_stats['bosses_slain'] += 1

def calculate_damage(base_damage, weapon_damage, enchantment_bonus, item_bonus, monster_element, user_element):
    attack = base_damage + weapon_damage + enchantment_bonus + item_bonus

    if is_strong_against(user_element, monster_element):
        damage = attack * 2
    elif is_weak_against(user_element, monster_element):
        damage = attack * 0.5
    else:
        damage = attack

    return damage

    if user_element == 'poison':
        dot = dot_values[user_stats['equipment']['weapon']['rarity']]
        damage += dot  # Add the DoT value to the damage

    return damage

def is_strong_against(element1, element2):
    interactions = {
        'fire': 'ice',
        'ice': 'electric',
        'electric': 'earth',
        'earth': 'fire',
        'spirit': 'darkness',
        'darkness': 'spirit',
        'poison': 'rage',
        'rage': 'poison',
        'neutral': None
    }

    return element1 == interactions[element2]

def calculate_damage(base_damage, weapon_damage, enchantment_bonus, item_bonus, monster_element, user_element):
    attack = base_damage + weapon_damage + enchantment_bonus + item_bonus

    if is_strong_against(user_element, monster_element):
        damage = attack * 2
    elif is_weak_against(user_element, monster_element):
        damage = attack * 0.5
    else:
        damage = attack

    return damage


difficulty_multiplier = 1.1
reward_multiplier = 1.75

while True:
    if cmd == "G":
        boss_health = 500 * (difficulty_multiplier ** user_stats['bosses_slain'])
        boss_attack = 350 * (difficulty_multiplier ** user_stats['bosses_slain'])

    user_stats['boss_attempts'] += 1


    if user_stats['boss_attempts'] >= 10 and not user_stats['pity_buff']:
        user_stats['stats']['attack'] *= 1.5  # Increase attack by 50%
        user_stats['stats']['defense'] *= 1.5  # Increase defense by 50%
        user_stats['pity_buff'] = True  # Set the pity buff flag
        print("You've received a pity buff! Your stats have temporarily been increased.")

async def process_boss_fight(ctx, user_id):
    boss_health = 250  # Base boss health
    boss_defense = 250  # Base boss defense
    boss_attack = 50  # Base boss attack

    user_attack = user_stats[user_id]['stats']['attack']
    user_defense = user_stats[user_id]['stats']['defense']
    user_element = user_stats[user_id]['stats']['element']

    user_damage = calculate_damage(user_attack, 'neutral', 'neutral')
    boss_health -= user_damage

    if cmd == "G":
        boss_health = 500 * (difficulty_multiplier ** user_stats['bosses_slain'])
        boss_attack = 350 * (difficulty_multiplier ** user_stats['bosses_slain'])

    if boss_health <= 0:
        user_stats['bosses_slain'] += 1
        reward = 100 * (reward_multiplier ** user_stats['bosses_slain'])
        user_stats['gold'] += reward
        print(f"You defeated the boss! You earned {reward} gold.")
        user_stats['boss_attempts'] = 0
        if user_stats['pity_buff']:
            user_stats['stats']['attack'] /= 1.5
            user_stats['stats']['defense'] /= 1.5
            user_stats['pity_buff'] = False

        print(f"You defeated the boss! You earned 100 gold.")
    else:
        boss_damage = calculate_damage(boss_attack, 'neutral', user_element)
        user_stats[user_id]['health'] -= boss_damage

        # Check if the user is defeated
        if user_stats[user_id]['health'] <= 0:
            print(f"You were defeated by the boss! Try again.")

while True:
    print("Welcome to the Text-based idle game!")
cmd = input("Do you want to (B)uy an item, (E)quip an item, (U)nequip an item, (S)ell an item, or (F)ight a monster? ")

if cmd.upper() == "B":
    # Call the function to handle buying an item
    buy_item()
elif cmd.upper() == "E":
    # Call the function to handle equipping an item
    equip_item()
elif cmd.upper() == "U":
    # Call the function to handle unequipping an item
    unequip_item()
elif cmd.upper() == "S":
    # Call the function to handle selling an item
    sell_item()
elif cmd.upper() == "F":
    # Call the function to handle fighting a monster
    fight_monster()
else:
    print("Invalid command. Please enter B, E, U, S or F.")

user_stats[user_id]['inventory'] = []

def add_to_inventory(item):
    if len(user_stats[user_id]['inventory']) < 20:
        user_stats[user_id]['inventory'].append(item)
        print(f"You've added {item} to your inventory.")
    else:
        print("Your inventory is full.")

def sell_item(item):
    if item in user_stats[user_id]['inventory']:
        sell_price = shop_items[item]['price'] / 2
        user_stats[user_id]['gold'] += sell_price
        user_stats[user_id]['inventory'].remove(item)
        print(f"You've sold {item} for {sell_price} gold. Total gold: {user_stats[user_id]['gold']}")
    else:
        print(f"You don't have {item} in your inventory.")

def remove_from_inventory(item):
    user_stats[user_id]['inventory'].remove(item)
    print(f"You've removed {item} from your inventory.")

    time.sleep(1.5)
    if cmd == "B":
        item_name = input("Enter the name of the item you want to buy: ")
        if item_name in shop_items:
            item_price = shop_items[item_name]['price']
            if user_stats['gold'] >= item_price:
                user_stats['gold'] -= item_price
                update_rarity(user_stats['bosses_slain'])
                user_stats['equipment'][item_name] = shop_items[item_name]
                print(f"You've bought {item_name} for {item_price} gold. Would you like to equip it? (yes/no)")
            else:
                print("Not enough gold to buy the item.")
        else:
            print(f"{item_name} is not available in the shop.")
    elif cmd == "E":
        item_name = input("Enter the name of the item you want to equip: ")
        if item_name in user_stats['equipment']:
            user_stats['stats']['element'] = user_stats['equipment'][item_name]['element']
            user_stats['stats']['attack'] += user_stats['equipment'][item_name].get('attack_bonus', 0)
            user_stats['stats']['defense'] += user_stats['equipment'][item_name].get('defense_bonus', 0)
            print(f"You've equipped {item_name} with {user_stats['stats']['element']} element. Bonuses added to stats.")
        else:
            print(f"You don't have {item_name} in your equipment.")
    elif cmd == "U":
        item_name = input("Enter the name of the item you want to unequip: ")
        if item_name in user_stats['equipment']:
            user_stats['stats']['element'] = None  # Unequipping removes element bonus
            user_stats['stats']['attack'] -= user_stats['equipment'][item_name].get('attack_bonus', 0)
            user_stats['stats']['defense'] -= user_stats['equipment'][item_name].get('defense_bonus', 0)
            print(f"You've unequipped {item_name}. Bonuses removed from stats.")
        else:
            print(f"You don't have {item_name} in your equipment.")
    elif cmd == "F":
        if random.random() < small_monster_spawn_chance:
            small_monster_element = random.choice(small_monster_elements)
            print(f"A wild {small_monster_element.capitalize()} Small Monster has appeared!")
            if 'element' in user_stats['stats']:
                user_element = user_stats['stats']['element']
                damage = calculate_damage(user_stats['stats']['attack'], small_monster_element, user_element)
            user_stats['small_monsters_defeated'] += 1


