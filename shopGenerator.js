import { ELEMENTS } from './constants.js';
import { RARITIES, MATERIALS } from './rarity.js';
import { ARMOR_ENCHANTMENTS, WEAPON_ENCHANTMENTS } from './enchantments.js';
import { SHOP_ITEMS } from './shop.js';
import { CONSUMABLES } from './consumables.js';
import { generateItemName } from './lootUtils.js';

function getCurrentRotationSeed(hours = 3) {
  const now = Date.now();
  const window = hours * 60 * 60 * 1000;
  return Math.floor(now / window);
}

function mulberry32(a) {
  return function () {
    a |= 0; a += 0x6D2B79F5; a |= 0;
    let t = Math.imul(a ^ a >>> 15, 1 | a);
    t ^= t + Math.imul(t ^ t >>> 7, 61 | t);
    return ((t ^ t >>> 14) >>> 0) / 4294967296;
  };
}

function shuffle(arr) {
  const copy = [...arr];
  for (let i = copy.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [copy[i], copy[j]] = [copy[j], copy[i]];
  }
  return copy;
}

function inferType(name) {
  const lower = name.toLowerCase();
  if (['sword', 'axe', 'bow', 'dagger', 'staff', 'hammer'].some(w => lower.includes(w))) return 'weapon';
  if (['helmet', 'robe', 'cloak', 'gauntlet', 'boots', 'chest', 'legs', 'sleeves'].some(w => lower.includes(w))) return 'armor';
  return 'misc';
}

function getRotatingGearPool() {
  const gearItems = Object.keys(SHOP_ITEMS).filter(itemName => !CONSUMABLES[itemName]);
  const seed = getCurrentRotationSeed();
  const rng = mulberry32(seed);
  const shuffled = [...gearItems].sort(() => rng() - 0.5);
  return shuffled.slice(0, 5);
}

function getRandomKey(obj) {
  const keys = Object.keys(obj);
  return keys[Math.floor(Math.random() * keys.length)];
}

function getRandomRarity([min, max]) {
  const minIndex = RARITIES.indexOf(min);
  const maxIndex = RARITIES.indexOf(max);
  const available = RARITIES.slice(minIndex, maxIndex + 1);
  return available[Math.floor(Math.random() * available.length)];
}

export function generateShopItem(itemName, type) {
  const materialName = getRandomKey(MATERIALS);
  const material = MATERIALS[materialName];
  const element = ELEMENTS[Math.floor(Math.random() * ELEMENTS.length)];
  const rarity = getRandomRarity(material.rarity);
  const basePrice = 150;
  const maxEnchantments = ['Cloth', 'Leather', 'Cloak', 'Robes', 'Broach', 'Bracelet'].includes(itemName) ? 2 : 1;

  const enchantments = [];
  if (material.canBeEnchanted) {
    const pool = type === 'weapon' ? Object.keys(WEAPON_ENCHANTMENTS) : Object.keys(ARMOR_ENCHANTMENTS);
    while (enchantments.length < maxEnchantments) {
      const enchant = pool[Math.floor(Math.random() * pool.length)];
      if (!enchantments.includes(enchant)) enchantments.push(enchant);
    }
  }

  const primaryEnchant = enchantments[0];
  const displayName = primaryEnchant ? generateItemName(itemName, { name: primaryEnchant }) : itemName;

  return {
    name: displayName,
    baseName: itemName,
    type,
    material: materialName,
    rarity,
    element,
    basePrice,
    enchantments
  };
}

export function generateShopForPlayer(player) {
  const staticItems = Object.keys(CONSUMABLES);
  const rotatingGear = getRotatingGearPool();
  const fullShopList = [...staticItems, ...rotatingGear];

  const shop = {};
  fullShopList.forEach(name => {
    const type = CONSUMABLES[name] ? 'consumable' : inferType(name);
    shop[name] = generateShopItem(name, type);
  });

  return shop;
}