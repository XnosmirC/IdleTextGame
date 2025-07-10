import { ELEMENTS } from './constants.js';
import { MATERIALS, RARITIES } from './rarity.js';
import { RARITY_MULTIPLIERS } from './constants.js';

export function updateShopItems(shop) {
  Object.values(shop).forEach(item => {
    const materialName = getRandomKey(MATERIALS);
    const material = MATERIALS[materialName];
    const rarity = randomFromRange(material.rarity, RARITIES);
    const element = ELEMENTS[Math.floor(Math.random() * ELEMENTS.length)];

    item.material = materialName;
    item.rarity = rarity;
    item.element = element;
    item.defense = getRandomInt(...material.defense);
    item.canBeEnchanted = material.canBeEnchanted;
    item.price = Math.round(item.basePrice * RARITY_MULTIPLIERS[rarity]);

    if (!item.name) item.name = `${rarity} ${item.material} ${item.baseName || 'Item'}`;
  });

}

function getRandomKey(obj) {
  const keys = Object.keys(obj);
  return keys[Math.floor(Math.random() * keys.length)];
}

function randomFromRange(range, list) {
  const [min, max] = range;
  const i = list.indexOf(min);
  const j = list.indexOf(max);
  const possible = list.slice(i, j + 1);
  return possible[Math.floor(Math.random() * possible.length)];
}

function getRandomInt(min, max) {
  return Math.floor(Math.random() * (max - min + 1)) + min;
}

export function incrementStats(stats, increment) {
  for (let stat in stats) {
    stats[stat] += increment;
  }
  return stats;
}

export function ensureShopItemCount(shop, typeList, count, generator) {
  const current = Object.keys(shop).filter(key => typeList.includes(key)).length;
  while (Object.keys(shop).filter(k => typeList.includes(k)).length < count) {
    const name = getRandomFromList(typeList);
    if (!shop[name]) {
      shop[name] = generator(name);
    }
    function getRandomFromList(list) {
      return list[Math.floor(Math.random() * list.length)];
    }
  }
}
return shop;