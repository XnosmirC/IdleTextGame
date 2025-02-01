import random
import time

# Define constants and base stats
base_user_stats = {'attack': 5, 'defense': 5, 'element': None, 'gold': 0}  # Added 'gold' to user stats
small_monster_spawn_chance = 0.75  # Define the spawn chance for small monsters
medium_monster_spawn_chance = 0.5  # Define the spawn chance for medium monsters
small_monster_elements = ['fire', 'ice', 'electric', 'earth', 'spirit', 'darkness', 'poison', 'rage', 'neutral']
small_monster_kills = 0  # Counter for small monster kills
gold_per_small_monster = 10  # Define how much gold the player earns for each small monster killed
medium_monster_elements = ['fire', 'ice', 'electric', 'earth', 'spirit', 'darkness', 'poison', 'rage', 'neutral']
medium_monster_kills = 0  # Counter for small monster kills
gold_per_medium_monster = 30  # Define how much gold the player earns for each small monster killed
price_multiplier = 1

# Define base stats for small and medium monsters
small_monster_base_stats = {'attack': 2, 'defense': 2, 'swing_speed': 1}
medium_monster_base_stats = {'attack': 5, 'defense': 7, 'swing_speed': 1.5}

# User stats
user_stats = {'points': 0, 'gold': 0, 'stats': base_user_stats.copy(), 'bosses_slain': 0, 'spells': {}, 'equipment': {}, 'health': 100, 'small_monsters_defeated': 0}
user_id = 'user'  # Replace with actual user id
# Initialize user_stats and user_id
user_id = 'user'
user_stats = {user_id: {'gold': 0, 'stats': base_user_stats.copy(), 'bosses_slain': 0, 'spells': {}, 'equipment': {}, 'health': 100, 'small_monsters_defeated': 0, 'potion_inventory': []}}

# Now you can use user_id to access and modify the user's stats

# Define a function to increment monster stats
def increment_monster_stats(monster_stats, increment):
    for stat in monster_stats:
        monster_stats[stat] += increment
    return monster_stats

# Increment small monster stats
small_monster_base_stats = increment_monster_stats(small_monster_base_stats, 1)

# Increment medium monster stats
medium_monster_base_stats = increment_monster_stats(medium_monster_base_stats, 2)

def kill_small_monster():
    global small_monster_kills
    small_monster_kills += 1
    base_user_stats['gold'] += gold_per_small_monster  # Increment the player's gold
    print(f"A small monster has been killed! You earned {gold_per_small_monster} gold. Total gold: {base_user_stats['gold']}")
    check_boss_spawn()

def kill_medium_monster():
    global medium_monster_kills
    medium_monster_kills += 1
    base_user_stats['gold'] += gold_per_medium_monster  # Increment the player's gold
    print(f"A medium monster has been killed! You earned {gold_per_medium_monster} gold. Total gold: {base_user_stats['gold']}")
    check_boss_spawn()

def spawn_small_monster(element):
    print(f"A small monster with element {element} has spawned!")

def spawn_medium_monster(element):
    print(f"A medium monster with element {element} has spawned!")

def spawn_monster(small_monster_spawn_chance, medium_monster_spawn_chance, monster_type):
    if monster_type == 'small':
        spawn_small_monster(element=random.choice(small_monster_elements))
    elif monster_type == 'medium':
        spawn_medium_monster(element=random.choice(medium_monster_elements))

def check_boss_spawn():
    global small_monster_kills, medium_monster_kills
    total_kills = small_monster_kills + medium_monster_kills
    if total_kills >= 25:
        small_monster_kills = 0  # Reset the counters
        medium_monster_kills = 0
        spawn_boss()

def spawn_boss():
    print("A boss has spawned!")

def defeat_boss():
    bonus_gold = int(base_user_stats['gold'] * 0.75)  # Calculate the bonus gold
    base_user_stats['gold'] += bonus_gold  # Increase the player's gold by 75%
    new_gold_per_kill = base_user_stats['gold'] / (small_monster_kills + medium_monster_kills + 1)  # Calculate the new gold earned per kill
    print(f"You defeated a boss! You earned a 75% bonus of {bonus_gold} gold. Total gold: {base_user_stats['gold']}. Now, gold earned per kill: {new_gold_per_kill}")

def add_to_inventory(item):  # Redefinition removed
    # Check if there's space in the inventory
    if len(user_stats[user_id]['inventory']) < 20:
        # Add the item to the inventory
        user_stats[user_id]['inventory'].append(item)
        print(f"You've added {item} to your inventory.")
    else:
        print("Your inventory is full.")

# Initialize the user's potion inventory as an empty list
user_stats[user_id]['potion_inventory'] = []

def add_potion_to_inventory(potion):
    # Check if there's space in the potion inventory
    if len(user_stats[user_id]['potion_inventory']) < 20:
        # Add the potion to the inventory
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

# Damage over time values for each rarity
dot_values = {
    'common': 1,
    'uncommon': 2,
    'rare': 3,
    'epic': 3,
    'legendary': 3,
    'unique': 3
}

# Rarity multipliers
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

# Rarities
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

# Armor and jewelry items
items = ['Helmet', 'Cloak', 'Robes', 'Chest', 'Paulders', 'Sleeves', 'Gauntlets', 'Legs', 'Boots', 'Necklace', 'Ring', 'Broach', 'Bracelet']

# Shop items data structure with rarity, elements, and materials
shop_items = {item: {'base_price': 150, 'material': random.choice(list(materials.keys())), 'rarity': random.choice(rarities), 'element': random.choice(elements), 'max_enchantments': 2 if item in ['Cloth', 'Leather', 'Cloak', 'Robes', 'Broach', 'Bracelet'] else 1} for item in items}

# Enchantments for weapons
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

# Enchantments for armor and jewelry
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

# Add enchantments to shop items
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

    # Check if the item is in the shop
    if item_name in shop_items:
        item_price = shop_items[item_name]['price']

        # Check if the user has enough gold to buy the item
        if user_stats[user_id]['gold'] >= item_price:
            user_stats[user_id]['gold'] -= item_price

            # Add the item to the user's inventory
            user_stats[user_id]['inventory'][item_name] = shop_items[item_name]

            print(f"You've bought {item_name} for {item_price} gold.")

            # Check if the purchased item is Pixie Cider or Asgardian Punch
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
        item['defense'] = random.randint(*materials[item['material']]['defense'])  # Set defense based on material
        item['can_be_enchanted'] = materials[item['material']]['can_be_enchanted']  # Set enchantability based on material
        item['price'] = item['base_price'] * rarity_multipliers[item['rarity']]  # Adjust price based on rarity

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

# Update shop_items to include the new items
shop_items.update(new_items)

def equip(item_name):
    user_id = 'user'  # Replace with actual user id

    # Check if the item is in the user's equipment
    if item_name in user_stats[user_id]['equipment']:
        # Check if the item is a Broach or Bracelet
        if item_name in ['Broach', 'Bracelet']:
            # Check if the user is wearing compatible armor
            if any(armor in user_stats[user_id]['equipment'] for armor in ['Cloth', 'Leather', 'Cloak', 'Robes']):
                user_stats[user_id]['stats']['element'] = user_stats[user_id]['equipment'][item_name]['element']
                # Add bonuses to stats based on equipped item
                user_stats[user_id]['stats']['defense'] += user_stats[user_id]['equipment'][item_name].get('defense_bonus', 0)
                print(f"You've equipped {item_name} with {user_stats[user_id]['stats']['element']} element. Bonuses added to stats.")
            else:
                print(f"You can't equip {item_name} without wearing Cloth, Leather, Cloak, or Robes.")
        else:
            user_stats[user_id]['stats']['element'] = user_stats[user_id]['equipment'][item_name]['element']
            # Add bonuses to stats based on equipped item
            user_stats[user_id]['stats']['attack'] += user_stats[user_id]['equipment'][item_name].get('attack_bonus', 0)
            user_stats[user_id]['stats']['defense'] += user_stats[user_id]['equipment'][item_name].get('defense_bonus', 0)
            print(f"You've equipped {item_name} with {user_stats[user_id]['stats']['element']} element. Bonuses added to stats.")
    else:
        print(f"You don't have {item_name} in your equipment.")

# Base stats for the weapons
weapon_stats = {
    'One Handed Sword': {'base_price': 150, 'swing_speed': 1, 'attacks_per_minute': 60, 'damage': 5},
    'Dual Blades': {'base_price': 200, 'swing_speed': 1.25, 'attacks_per_minute': 75, 'damage': 10},
    'Two Handed Sword': {'base_price': 250, 'swing_speed': 0.75, 'attacks_per_minute': 45, 'damage': 12},
    'Recurve Bow': {'base_price': 100, 'reload_speed': 0.50, 'attacks_per_minute': 30, 'damage': 3},
    'Compound Bow': {'base_price': 150, 'reload_speed': 0.50, 'attacks_per_minute': 30, 'damage': 4},
    'Crossbow': {'base_price': 300, 'speed': 0.25, 'attacks_per_minute': 15, 'damage': 12},
    'Staff': {'base_price': 225, 'swing_speed': 1.25, 'attacks_per_minute': 125, 'damage': 7},
    'Mage Staff': {'base_price': 200, 'magic_speed': 1, 'attacks_per_minute': 60, 'damage': 4},
    'One Handed Axe': {'base_price': 200, 'swing_speed': 0.75, 'attacks_per_minute': 45, 'damage': 6},
    'Two Handed Heavy Axe': {'base_price': 350, 'swing_speed': 0.25, 'attacks_per_minute': 15, 'damage': 15},
    'Dual Axes': {'base_price': 300, 'swing_speed': 1, 'attacks_per_minute': 60, 'damage': 12},
    'One Handed Hammer': {'base_price': 200, 'swing_speed': 0.75, 'attacks_per_minute': 45, 'damage': 7},
    'Dual Hammers': {'base_price': 225, 'swing_speed': 0.85, 'attacks_per_minute': 60, 'damage': 11},
    'Two Handed Hammer': {'base_price': 350, 'swing_speed': 0.25, 'attacks_per_minute': 15, 'damage': 16},
    'Dagger': {'base_price': 100, 'swing_speed': 1.75, 'attacks_per_minute': 105, 'damage': 3},
    'Dual Daggers': {'base_price': 200, 'swing_speed': 1.5, 'attacks_per_minute': 90, 'damage': 5},
    'One Handed Mace': {'base_price': 200, 'swing_speed': 0.7, 'attacks_per_minute': 40, 'damage': 8},
    'Dual Maces': {'base_price': 275, 'swing_speed': 0.8, 'attacks_per_minute': 55, 'damage': 9},
    'Two Handed Mace': {'base_price': 375, 'swing_speed': 0.2, 'attacks_per_minute': 12, 'damage': 18},
    'One Handed Flail': {'base_price': 175, 'swing_speed': 1.25, 'attacks_per_minute': 100, 'damage': 12},
    'Dual Flails': {'base_price': 225, 'swing_speed': 1.75, 'attacks_per_minute': 150, 'damage': 16},
    'Two Handed Flail': {'base_price': 425, 'swing_speed': 1, 'attacks_per_minute': 60, 'damage': 20, 'strength': 35},
    'Glaive': {'base_price': 100, 'swing_speed': 1, 'attacks_per_minute': 60, 'damage': 8},
    'Double-Ended Glaive': {'base_price': 125, 'swing_speed': 125, 'attacks_per_minute': 75, 'damage': 12},
}

# Shop items data structure with rarity and elements
shop_items = {weapon: {**stats, 'rarity': random.choice(rarities), 'element': random.choice(elements)} for weapon, stats in weapon_stats.items()}

# Categorize your items
weapons = ['One Handed Sword', 'Dual Blades', 'Two Handed Sword', 'Recurve Bow', 'Compound Bow', 'Crossbow', 'Staff', 'Mage Staff', 'One Handed Axe', 'Two Handed Heavy Axe', 'Dual Axes', 'One Handed Hammer', 'Dual Hammers' 'Two Handed Hammer', 'Dagger', 'Dual Daggers', 'One Handed Mace', 'Dual Maces', 'Two Handed Mace', 'One Handed Flail', 'Dual Flails', 'Two Handed Flail', 'Glaive', 'Double-Ended Glaive']
armor = ['Helmet', 'Cloak', 'Robes', 'Chest', 'Paulders', 'Sleeves', 'Gauntlets', 'Legs', 'Boots', 'Necklace', 'Ring', 'Broach', 'Bracelet']

# Define rarity milestones
rarity_milestones = {
    'common': 0,
    'uncommon': 15,
    'rare': 45,
    'epic': 125,
    'legendary': 250,
    'unique': 550
}

def update_rarity(bosses_slain):
    # Determine the highest rarity available based on bosses defeated
    available_rarities = [rarity for rarity, milestone in rarity_milestones.items() if bosses_slain >= milestone]
    return available_rarities

# Example function to update shop items including rarity based on bosses slain
def update_shop_items(user_id):
    available_rarities = update_rarity(user_stats[user_id]['bosses_slain'])
    for item in shop_items.values():
        item['material'] = random.choice(list(materials.keys()))
        item['rarity'] = random.choice(available_rarities)
        item['element'] = random.choice(elements)
        item['defense'] = random.randint(*materials[item['material']]['defense'])  # Set defense based on material
        item['can_be_enchanted'] = materials[item['material']]['can_be_enchanted']  # Set enchantability based on material
        item['price'] = item['base_price'] * price_multiplier * rarity_multipliers[item['rarity']]  # Adjust price based on rarity and multiplier

def update_shop_items():
    weapon_count = 0
    armor_count = 0

    # Count the number of weapons and armor in the shop
    for item in shop_items:
        if item in weapons:
            weapon_count += 1
        elif item in armor:
            armor_count += 1

    # Add weapons if there are less than three
    while weapon_count < 3:
        weapon = random.choice(weapons)
        if weapon not in shop_items:
            shop_items[weapon] = {'base_price': 150, 'material': random.choice(list(materials.keys())), 'rarity': random.choice(rarities), 'element': random.choice(elements), 'max_enchantments': 1}
            weapon_count += 1

    # Add armor if there are less than three
    while armor_count < 3:
        piece = random.choice(armor)
        if piece not in shop_items:
            shop_items[piece] = {'base_price': 150, 'material': random.choice(list(materials.keys())), 'rarity': random.choice(rarities), 'element': random.choice(elements), 'max_enchantments': 2 if piece in ['Cloth', 'Leather', 'Cloak', 'Robes', 'Broach', 'Bracelet'] else 1}
            armor_count += 1

    # Update the rest of the items
    for item in shop_items.values():
        item['rarity'] = random.choice(rarities)
        item['element'] = random.choice(elements)
        item['price'] = item['base_price'] * rarity_multipliers[item['rarity']]  # Adjust price based on rarity

# Check if the item is in the shop
if item_name in shop_items:
    item_price = shop_items[item_name]['price']
    pass
for key in item_name:
    if key in shop_items:
        pass  

# Check if the user has enough gold to buy the item
if item_name not in shop_items:
    print(f"{item_name} is not available in the shop. Check back later!")
elif user_stats[user_id]['gold'] < item_price:
    print("Not enough gold to buy the item.")
else:
    user_stats[user_id]['gold'] -= item_price
    # Increment the price multiplier by 1%
    price_multiplier += 0.1

if item_name not in shop_items:
    print(f"{item_name} is not available in the shop. Check back later!")
elif user_stats[user_id]['gold'] < item_price:
    print("Not enough gold to buy the item.")
else:
    user_stats[user_id]['gold'] -= item_price
    # Increment the price multiplier by 1%
    price_multiplier += 0.1

    # Update rarity based on bosses defeated
    update_rarity(user_stats[user_id]['bosses_slain'])

    # Add the item to the user's equipment
    user_stats[user_id]['equipment'][item_name] = shop_items[item_name]

    print(f"You've bought {item_name} for {item_price} gold. Would you like to equip it? (yes/no)")

# User stats
user_stats = {'points': 0, 'gold': 0, 'stats': base_user_stats.copy(), 'bosses_slain': 0, 'spells': {}, 'equipment': {}, 'health': 100, 'small_monsters_defeated': 0}

if random.random() < 0.75:  # Assuming small_monster_spawn_chance is 0.75
    small_monster_element = random.choice(small_monster_elements)
    print(f"A wild {small_monster_element.capitalize()} Small Monster has appeared!")

if random.random() < medium_monster_spawn_chance:
    medium_monster_element = random.choice(medium_monster_elements)
    print(f"A wild {medium_monster_element.capitalize()} medium Monster has appeared!")

# Function to update rarity based on bosses defeated
def update_rarity(bosses_defeated):
    user_stats['bosses_slain'] += 1  # Increment the counter

# Function to calculate damage considering element interactions
def calculate_damage(base_damage, weapon_damage, enchantment_bonus, item_bonus, monster_element, user_element):
    # Calculate total attack power
    attack = base_damage + weapon_damage + enchantment_bonus + item_bonus

    # If the user's element is strong against the monster's element, deal damage and a half
    if is_strong_against(user_element, monster_element):
        damage = attack * 2
    # If the user's element is weak against the monster's element, deal half damage
    elif is_weak_against(user_element, monster_element):
        damage = attack * 0.5
    else:
        damage = attack

    return damage

    # If the user's element is poison, apply the DoT effect
    if user_element == 'poison':
        dot = dot_values[user_stats['equipment']['weapon']['rarity']]  # Get the DoT value based on the weapon's rarity
        damage += dot  # Add the DoT value to the damage

    return damage

# Function to check if one element is strong against another
def is_strong_against(element1, element2):
    # Define your element interactions here
    # Example: Fire is strong against Ice
    interactions = {
        'fire': 'ice',
        'ice': 'electric',
        'electric': 'earth',
        'earth': 'fire',
        'spirit': 'darkness',
        'darkness': 'spirit',
        'poison': 'rage',
        'rage': 'poison',
        'neutral': None  # Neutral has no strengths or weaknesses
    }

    return element1 == interactions[element2]

def is_weak_against(element1, element2):
    # Define your element interactions here
    # Example: Fire is weak against Earth
    interactions = {
        'fire': 'earth',
        'ice': 'fire',
        'electric': 'ice',
        'earth': 'electric',
        'spirit': 'darkness',
        'darkness': 'spirit',
        'poison': 'rage',
        'rage': 'poison',
        'neutral': None  # Neutral has no strengths or weaknesses
    }

    return element1 == interactions[element2]
    # Define your element interactions here
    # Example: Fire is strong against Ice
    interactions = {
        'fire': 'ice',
        'ice': 'electric',
        'electric': 'earth',
        'earth': 'fire',
        'spirit': 'darkness',
        'darkness': 'spirit',
        'poison': 'rage',
        'rage': 'poison',
        'neutral': None  # Neutral has no strengths or weaknesses
    }

    return element1 == interactions[element2]

def calculate_damage(base_damage, weapon_damage, enchantment_bonus, item_bonus, monster_element, user_element):
    # Calculate total attack power
    attack = base_damage + weapon_damage + enchantment_bonus + item_bonus

    # If the user's element is strong against the monster's element, deal damage and a half
    if is_strong_against(user_element, monster_element):
        damage = attack * 2
    # If the user's element is weak against the monster's element, deal half damage
    elif is_weak_against(user_element, monster_element):
        damage = attack * 0.5
    else:
        damage = attack

    return damage


difficulty_multiplier = 1.1  # Enemies get 10% harder each time
reward_multiplier = 1.75  # Rewards increase by 75% each time

while True:
    # Your game code...
    cmd = input("Enter your command: ")
    if cmd == "G":
        # Boss fight process...
        boss_health = 500 * (difficulty_multiplier ** user_stats['bosses_slain'])  # Increase boss health
        boss_attack = 350 * (difficulty_multiplier ** user_stats['bosses_slain'])  # Increase boss attack

    user_stats['boss_attempts'] += 1  # Increase the boss attempts counter

    # Check if the player is eligible for the pity buff
    if user_stats['boss_attempts'] >= 10 and not user_stats['pity_buff']:
        user_stats['stats']['attack'] *= 1.5  # Increase attack by 50%
        user_stats['stats']['defense'] *= 1.5  # Increase defense by 50%
        user_stats['pity_buff'] = True  # Set the pity buff flag
        print("You've received a pity buff! Your stats have been increased.")

# Loop for processing boss fights
async def process_boss_fight(ctx, user_id):
    boss_health = 250  # Base boss health
    boss_defense = 250  # Base boss defense
    boss_attack = 50  # Base boss attack

    user_attack = user_stats[user_id]['stats']['attack']
    user_defense = user_stats[user_id]['stats']['defense']
    user_element = user_stats[user_id]['stats']['element']

    # Calculate damage dealt by the user to the boss
    user_damage = calculate_damage(user_attack, 'neutral', 'neutral')  # Assuming the boss has neutral element
    boss_health -= user_damage

    if cmd == "G":
        # Boss fight process...
        boss_health = 500 * (difficulty_multiplier ** user_stats['bosses_slain'])  # Increase boss health
        boss_attack = 350 * (difficulty_multiplier ** user_stats['bosses_slain'])  # Increase boss attack

    # Check if the boss is defeated
    if boss_health <= 0:
        # User wins the boss fight
        user_stats['bosses_slain'] += 1
        reward = 100 * (reward_multiplier ** user_stats['bosses_slain'])
        user_stats['gold'] += reward
        print(f"You defeated the boss! You earned {reward} gold.")
        user_stats['boss_attempts'] = 0
        if user_stats['pity_buff']:
            user_stats['stats']['attack'] /= 1.5  # Decrease attack back to normal
            user_stats['stats']['defense'] /= 1.5  # Decrease defense back to normal
            user_stats['pity_buff'] = False  # Reset the pity buff flag

        print(f"You defeated the boss! You earned 100 gold.")
    else:
        # Boss attacks the user
        boss_damage = calculate_damage(boss_attack, 'neutral', user_element)  # Assuming the boss has neutral element
        user_stats[user_id]['health'] -= boss_damage

        # Check if the user is defeated
        if user_stats[user_id]['health'] <= 0:
            print(f"You were defeated by the boss! Try again.")

# Game loop
while True:
    print("Welcome to Crimson's RPG game!")
    
    # Prompt the player for a command
    cmd = input("Do you want to (B)uy an item, (E)quip an item, (U)nequip an item, (S)ell an item, or (F)ight a monster? ")

    # Handle the command
    if cmd.upper() == "B":
        # Call the function to handle buying an item
        buy(input("Enter the name of the item you want to buy: "))
    elif cmd.upper() == "E":
        # Call the function to handle equipping an item
        equip(input("Enter the name of the item you want to equip: "))
    elif cmd.upper() == "U":
        # Call the function to handle unequipping an item
        unequip(input("Enter the name of the item you want to unequip: "))
    elif cmd.upper() == "S":
        # Call the function to handle selling an item
        sell(input("Enter the name of the item you want to sell: "))
    elif cmd.upper() == "F":
        # Call the function to handle fighting a monster
        fight()
    else:
        print("Invalid command. Please enter B, E, U, S, or F.")


# Initialize the user's inventory as an empty list
user_stats[user_id]['inventory'] = []

def add_to_inventory(item):
    # Check if there's space in the inventory
    if len(user_stats[user_id]['inventory']) < 20:
        # Add the item to the inventory
        user_stats[user_id]['inventory'].append(item)
        print(f"You've added {item} to your inventory.")
    else:
        print("Your inventory is full.")

def sell_item(item):
    # Check if the item is in the user's inventory
    if item in user_stats[user_id]['inventory']:
        # Calculate the sell price as half the buy price
        sell_price = shop_items[item]['price'] / 2
        # Add the sell price to the user's gold
        user_stats[user_id]['gold'] += sell_price
        # Remove the item from the user's inventory
        user_stats[user_id]['inventory'].remove(item)
        print(f"You've sold {item} for {sell_price} gold. Total gold: {user_stats[user_id]['gold']}")
    else:
        print(f"You don't have {item} in your inventory.")

def remove_from_inventory(item):
    # Remove the item from the inventory
    user_stats[user_id]['inventory'].remove(item)
    print(f"You've removed {item} from your inventory.")

    time.sleep(1.5)  # Wait for 1.5 seconds
    if cmd == "B":
        item_name = input("Enter the name of the item you want to buy: ")
        # Check if the item is in the shop
        if item_name in shop_items:
            item_price = shop_items[item_name]['price']
            # Check if the user has enough gold to buy the item
            if user_stats['gold'] >= item_price:
                user_stats['gold'] -= item_price
                # Update rarity based on bosses defeated
                update_rarity(user_stats['bosses_slain'])
                # Add the item to the user's equipment
                user_stats['equipment'][item_name] = shop_items[item_name]
                print(f"You've bought {item_name} for {item_price} gold. Would you like to equip it? (yes/no)")
            else:
                print("Not enough gold to buy the item.")
        else:
            print(f"{item_name} is not available in the shop.")
    elif cmd == "E":
        item_name = input("Enter the name of the item you want to equip: ")
        # Check if the item is in the user's equipment
        if item_name in user_stats['equipment']:
            user_stats['stats']['element'] = user_stats['equipment'][item_name]['element']
            # Add bonuses to stats based on equipped item
            user_stats['stats']['attack'] += user_stats['equipment'][item_name].get('attack_bonus', 0)
            user_stats['stats']['defense'] += user_stats['equipment'][item_name].get('defense_bonus', 0)
            print(f"You've equipped {item_name} with {user_stats['stats']['element']} element. Bonuses added to stats.")
        else:
            print(f"You don't have {item_name} in your equipment.")
    elif cmd == "U":
        item_name = input("Enter the name of the item you want to unequip: ")
        # Check if the item is in the user's equipment
        if item_name in user_stats['equipment']:
            # Remove the item from the user's equipment
            user_stats['stats']['element'] = None  # Unequipping removes element bonus
            # Remove bonuses from stats based on unequipped item
            user_stats['stats']['attack'] -= user_stats['equipment'][item_name].get('attack_bonus', 0)
            user_stats['stats']['defense'] -= user_stats['equipment'][item_name].get('defense_bonus', 0)
            print(f"You've unequipped {item_name}. Bonuses removed from stats.")
        else:
            print(f"You don't have {item_name} in your equipment.")
    elif cmd == "F":
        # Small Monster Encounter
        if random.random() < small_monster_spawn_chance:
            small_monster_element = random.choice(small_monster_elements)
            print(f"A wild {small_monster_element.capitalize()} Small Monster has appeared!")
            # Check if the user has equipped an item with an element
            if 'element' in user_stats['stats']:
                user_element = user_stats['stats']['element']
                # Calculate hits, damage, gold, and other combat mechanics against the small monster based on its element and user's weapon element
                damage = calculate_damage(user_stats['stats']['attack'], small_monster_element, user_element)
            user_stats['small_monsters_defeated'] += 1


