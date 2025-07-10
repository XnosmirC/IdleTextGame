import { CONSUMABLES, applyItemEffect } from './consumables.js';
import { MATERIALS, RARITIES, updateAvailableRarities } from './rarity.js';
import { ELEMENTS, RARITY_MULTIPLIERS } from './constants.js';
import { generateItemName } from './lootUtils.js'; // make sure this exists
import { getEnchantmentPool, isEnchantmentAllowed } from './enchantments.js'; // your custom logic
import { getBaseItemByRarity } from './lootTables.js'; // loot logic
import { shuffle } from './utils.js'; // safe shuffle if you use multi-enchant

export const SHOP_ITEMS = {
  'Health Potion': {},
  'Antidote': {},
  'Weakness to {element} potion': {},
  'Extra Weakness to {element} potion': {},
  'Advanced Weakness to {element} potion': {},
  'Supreme Weakness to {element} potion': {},
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
};

// Generates randomized shop stats for a player
export function updateShopItemsForPlayer(player, shopItems, priceMultiplier = 1) {
  const availableRarities = updateAvailableRarities(player.bossesSlain);
  const enchantmentPool = getEnchantmentPool();

  for (const [itemName, item] of Object.entries(shopItems)) {
    const mat = getRandomKey(MATERIALS);
    item.name = itemName;
    item.material = mat;
    item.rarity = getRandomFromList(availableRarities);
    item.element = getRandomFromList(ELEMENTS);
    item.basePrice = item.basePrice || 100;
    item.defense = getRandomInt(...MATERIALS[mat].defense);
    item.canBeEnchanted = MATERIALS[mat].canBeEnchanted;

    // Optional 15% enchantment chance
    if (item.canBeEnchanted && Math.random() < 0.15) {
      const validEnchantments = enchantmentPool.filter(e =>
        isEnchantmentAllowed(item.type || 'generic', e.name)
      );
      const enchantment = getRandom(validEnchantments);
      item.enchantment = enchantment;
      item.name = generateItemName(itemName, enchantment);
    }

    item.price = Math.round(item.basePrice * priceMultiplier * RARITY_MULTIPLIERS[item.rarity]);
  }
}

// Handles purchasing both consumables and equipment
export function purchaseItem(player, itemName, shopItems, priceMultiplierRef) {
  const item = shopItems[itemName] || CONSUMABLES[itemName];
  if (!item) {
    console.log(`${itemName} not found.`);
    return;
  }

  const price = Math.round(item.price * (priceMultiplierRef?.value || 1));
  if (player.gold < price) {
    console.log("Not enough gold to purchase that item.");
    return;
  }

  player.gold -= price;
  console.log(`Purchased ${item.name || itemName} for ${price} gold.`);

  if (item.instantUse) {
    applyItemEffect(player, itemName);
    return;
  }

  player.inventory.add({ name: itemName, ...item });
  priceMultiplierRef.value += 0.1;
}

function getRandomFromList(list) {
  return list[Math.floor(Math.random() * list.length)];
}

function getRandomKey(obj) {
  const keys = Object.keys(obj);
  return keys[Math.floor(Math.random() * keys.length)];
}

function getRandom(arr) {
  return arr[Math.floor(Math.random() * arr.length)];
}