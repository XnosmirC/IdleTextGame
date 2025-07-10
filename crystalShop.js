export const CRYSTAL_SHOP_ITEMS = {
  'Auric Crown': {
    description: 'Boosts gold gain by 0.01%.',
    effects: { goldBoost: 0.01 },
    cost: 300,
    level: 1,
    maxLevel: 50000,
    scaling: 0.05,
    type: 'relic'
  },
  'Crystal Nexus': {
    description: 'Earn +0.01% more Elemental Crystals per prestige.',
    effects: { crystalBoost: 0.001 },
    cost: 800,
    level: 1,
    maxLevel: 50000,
    scaling: 0.01,
    type: 'relic'
  },
  'Inferno Shard': {
    description: 'Increases damage for Fire and Ice elements by 15%.',
    effects: { elementBoosts: ['Fire', 'Ice'] },
    cost: 5000,
    level: 1,
    maxLevel: 3,
    type: 'relic'
  },
  'Stormcore Totem': {
    description: 'Increases damage for Electric and Earth elements by 15%.',
    effects: { elementBoosts: ['Electric', 'Earth'] },
    cost: 5000,
    level: 1,
    maxLevel: 3,
    type: 'relic'
  },
  'Wraithglass Medallion': {
    description: 'Increases damage for Spirit and Darkness elements by 30%.',
    effects: { elementBoosts: ['Spirit', 'Darkness'] },
    cost: 7500,
    level: 1,
    maxLevel: 3,
    type: 'relic'
  },
  'Venombark Emblem': {
    description: 'Increases damage for Poison and Rage elements by 15%.',
    effects: { elementBoosts: ['Poison', 'Rage'] },
    cost: 5000,
    level: 1,
    maxLevel: 3,
    type: 'relic'
  },
  'Equilibrium Sigil': {
    description: 'Increases damage for Neutral element by 25%.',
    effects: { elementBoosts: ['Neutral'] },
    cost: 3500,
    level: 1,
    maxLevel: 4,
    type: 'relic'
  }
};

export function purchaseCrystalItem(player, itemName) {
  const item = CRYSTAL_SHOP_ITEMS[itemName];
  if (!item) return console.log("That item doesn't exist.");
  if (player.crystals < item.cost) return console.log("Not enough Elemental Crystals.");
  if (!player.crystalItems) player.crystalItems = {};
  if (player.crystalItems[itemName]) return console.log(`${itemName} already purchased.`);

  if (!player.relicTabUnlocked) {
    player.relicTabUnlocked = true;
    console.log("✨ Relic tab unlocked! View your eternal upgrades from the Equipment screen.");
  }

  player.crystals -= item.cost;
  player.crystalItems[itemName] = {
    level: item.level,
    ...item.effects
  };

  console.log(`You acquired ${itemName}!`);
  console.log(`Effect: ${item.description}`);
}

export function upgradeCrystalItem(player, itemName) {
  const owned = player.crystalItems?.[itemName];
  const base = CRYSTAL_SHOP_ITEMS[itemName];
  if (!owned || !base) return console.log("Item not owned or missing.");
  if (owned.level >= base.maxLevel) return console.log("Already at max level.");

  const cost = getUpgradeCost(owned.level + 1);
  if (player.ingots < cost) return console.log(`You need ${cost} ingots to upgrade.`);

  player.ingots -= cost;
  owned.level++;

  for (let key in base.effects) {
    if (typeof base.effects[key] === 'number') {
      owned[key] = base.effects[key] + base.scaling * (owned.level - 1);
    }
  }

  console.log(`${itemName} upgraded to level ${owned.level}!`);
}

export function getUpgradeCost(level) {
  return Math.floor((level ** 1.7) + level); // Exponential cost curve
}