export const CONSUMABLES = {
  'Health Potion': {
    price: 10,
    effect: { restore_health_percent: 0.20 }, // Replenishment, not buff
    stackable: true,
    stackLimit: 10
  },
  'Magic Potion': {
    price: 10,
    effect: { restore_magic_percent: 0.20 },
    stackable: true,
    stackLimit: 10
  },
  'Antidote': {
    price: 12,
    effect: { negate_poison: true },
    stackable: true,
    stackLimit: 10
  },

  'Cure': {
    price: 15,
    effect: { negate_debuff: true },
    stackable: true,
    stackLimit: 10
  },

'Phoenix Feather': {
  price: 25000,
  effect: { auto_revive: true },
  rarity: 'legendary',
  stackable: false,
  maxPerInventory: 1,
  shopAvailability: 'rare'
},

'Weakness to {element} potion': {
  price: 1500,
  effect: { extra_damage_multiplier: 1.15 }, // +15% damage
  duration: 3,
  endsOnMonsterDeath: true,
  stackable: true,
  stackLimit: 3
},
'Extra Weakness to {element} potion': {
  price: 3000,
  effect: { extra_damage_multiplier: 1.30 }, // +30% damage
  duration: 3,
  endsOnMonsterDeath: true,
  stackable: true,
  stackLimit: 3
},
'Advanced Weakness to {element} potion': {
  price: 4500,
  effect: { extra_damage_multiplier: 1.45 }, // +45% damage
  duration: 3,
  endsOnMonsterDeath: true,
  stackable: true,
  stackLimit: 3
},
'Supreme Weakness to {element} potion': {
  price: 15000,
  effect: { extra_damage_multiplier: 2.50 }, // +150% damage
  duration: 3,
  endsOnMonsterDeath: true,
  stackable: true,
  stackLimit: 3
},
  'Apple Dumpling': {
    price: 5,
    effect: { restore_health_flat: 10, bow_damage_boost: 0.05 },
    duration: 3,
    endsOnMonsterDeath: true,
    stackable: true,
    stackLimit: 15
  },
  'Beef Stew': {
    price: 3,
    effect: { restore_health_flat: 8 },
    stackable: true,
    stackLimit: 10
  },
  'Baked Potatoes': {
    price: 1,
    effect: { restore_health_flat: 5 },
    stackable: true,
    stackLimit: 20
  },
  'Pixie Cider': {
      price: 20000,
      effect: { rage_damage_boost: 150 },
      instantUse: true
    },
    'Orcish Rotgut Ale': {
      price: 15000,
      effect: { poison_damage_boost: 100 },
      instantUse: true
    },
    'Asgardian Punch': {
      price: 20000,
      effect: { spirit_damage_boost: 150 },
      instantUse: true
    },
    'Party Popper Champagne': {
      price: 15000,
      effect: { electric_damage_boost: 100 },
      instantUse: true
    },
    'Dragon\'s Breath Mead': {
      price: 15000,
      effect: { fire_damage_boost: 100 },
      instantUse: true
    },
    'Spiced Wine': {
      price: 15000,
      effect: { neutral_damage_boost: 150 },
      instantUse: true
    },
    'Juniper\'s Brew': {
      price: 15000,
      effect: { earth_damage_boost: 100 },
      instantUse: true
    },
    'Undercroft Ale': {
      price: 15000,
      effect: { darkness_damage_boost: 100 },
      instantUse: true
    },
    'Iced Lager': {
      price: 15000,
      effect: { ice_damage_boost: 100 },
      instantUse: true
    },
    'Clear Honey': {
      price: 25,
      effect: { neutral_damage_boost: 15 },
      instantUse: true
    },
    'Clear Ambrosia': {
      price: 8500,
      effect: { neutral_damage_boost: 175 },
      instantUse: true
    },
    'Clear Jelly': {
      price: 450,
      effect: { neutral_damage_boost: 75 },
      instantUse: true
    },
    'Red Honey': {
      price: 25,
      effect: { rage_damage_boost: 10 },
      instantUse: true
    },
    'Red Ambrosia': {
      price: 8500,
      effect: { rage_damage_boost: 25 },
      instantUse: true
    },
    'Red Jelly': {
      price: 450,
      effect: { rage_damage_boost: 15 },
      instantUse: true
    },
    'Green Honey': {
      price: 25,
      effect: { earth_damage_boost: 10 },
      instantUse: true
    },
    'Green Ambrosia': {
      price: 8500,
      effect: { earth_damage_boost: 25 },
      instantUse: true
    },
    'Green Jelly': {
      price: 450,
      effect: { earth_damage_boost: 15 },
      instantUse: true
    },
    'Blue Honey': {
      price: 25,
      effect: { ice_damage_boost: 10 },
      instantUse: true
    },
    'Blue Ambrosia': {
      price: 8500,
      effect: { ice_damage_boost: 25 },
      instantUse: true
    },
    'Blue Jelly': {
      price: 450,
      effect: { ice_damage_boost: 15 },
      instantUse: true
    },
    'White Honey': {
      price: 25,
      effect: { spirit_damage_boost: 10 },
      instantUse: true
    },
    'White Ambrosia': {
      price: 8500,
      effect: { spirit_damage_boost: 25 },
      instantUse: true
    },
    'White Jelly': {
      price: 450,
      effect: { spirit_damage_boost: 15 },
      instantUse: true
    },
    'Black Honey': {
      price: 25,
      effect: { darkness_damage_boost: 10 },
      instantUse: true
    },
    'Black Ambrosia': {
      price: 8500,
      effect: { darkness_damage_boost: 25 },
      instantUse: true
    },
    'Black Jelly': {
      price: 450,
      effect: { darkness_damage_boost: 15 },
      instantUse: true
    },
    'Yellow Honey': {
      price: 25,
      effect: { electric_damage_boost: 10 },
      instantUse: true
    },
    'Yellow Ambrosia': {
      price: 8500,
      effect: { electric_damage_boost: 25 },
      instantUse: true
    },
    'Yellow Jelly': {
      price: 450,
      effect: { electric_damage_boost: 15 },
      instantUse: true
    },
    'Orange Honey': {
      price: 25,
      effect: { fire_damage_boost: 10 },
      instantUse: true
    },
    'Orange Ambrosia': {
      price: 8500,
      effect: { fire_damage_boost: 25 },
      instantUse: true
    },
    'Orange Jelly': {
      price: 450,
      effect: { fire_damage_boost: 15 },
      instantUse: true
    },
    'Purple Honey': {
      price: 25,
      effect: { poison_damage_boost: 10 },
      instantUse: true
    },
    'Purple Ambrosia': {
      price: 8500,
      effect: { poison_damage_boost: 25 },
      instantUse: true
    },
    'Purple Jelly': {
      price: 450,
      effect: { poison_damage_boost: 15 },
      instantUse: true
    }
  };


export function useConsumable(player, itemName) {
  const maxUses = 3;

  if (player.consumableUses[itemName] >= maxUses) {
    console.log(`${itemName} has reached its maximum ${maxUses} uses.`);
    return;
  }

  applyItemEffect(player, itemName);

  player.consumableUses[itemName] = (player.consumableUses[itemName] || 0) + 1;
  console.log(`${itemName} used (${player.consumableUses[itemName]}/${maxUses}).`);
}

function applyItemEffect(player, itemName) {
  const effect = CONSUMABLES[itemName]?.effect;
  if (!effect) return;

  if (effect.health_boost) {
    player.health += typeof effect.health_boost === 'number' && effect.health_boost < 1
      ? Math.floor(player.health * effect.health_boost)
      : effect.health_boost;
    console.log(`${itemName} restored health!`);
  }
}

function applyItemEffect(player, itemName) {
  const item = CONSUMABLES[itemName];
  const effect = item?.effect;
  if (!effect) return;

  const logEffect = (msg) => console.log(`🔸 ${msg}`);

  if (effect.health_boost) {
    const amount = effect.health_boost < 1
      ? Math.floor(player.health * effect.health_boost)
      : effect.health_boost;
    player.health += amount;
    logEffect(`${itemName} restored ${amount} health.`);
  }

  if (effect.magic_boost) {
    player.magic = (player.magic || 0) + Math.floor(player.magic * effect.magic_boost);
    logEffect(`${itemName} boosted your magic.`);
  }

  if (effect.negate_poison) {
    player.isPoisoned = false;
    logEffect(`${itemName} cured poison.`);
  }

  for (const key in effect) {
    if (key.endsWith('_damage_boost')) {
      const element = key.split('_damage_boost')[0];
      player.damageBoosts = player.damageBoosts || {};
      player.damageBoosts[element] = (player.damageBoosts[element] || 0) + effect[key];
      logEffect(`${itemName} boosted ${element} damage by ${effect[key]}.`);
    }
  }

  if (effect.extra_damage) {
    player.flatBonusDamage = (player.flatBonusDamage || 0) + effect.extra_damage;
    logEffect(`${itemName} granted +${effect.extra_damage} bonus damage.`);
  }

  if (effect.bow_damage_boost) {
    player.bowDamageBonus = (player.bowDamageBonus || 0) + effect.bow_damage_boost;
    logEffect(`${itemName} increased bow damage by ${effect.bow_damage_boost * 100}%.`);
  }
}