export const WEAPON_ENCHANTMENTS = {
  'Absorb Health': { extraDamage: -1 },
  'Absorb Magic': { magicAbsorption: 10 },
  'Banish': { banish: true },
  'Fear': { fear: true },
  'Fire Damage': { extraDamage: 10, burn: true },
  'Ice Damage': { extraDamage: 5, slow: 0.25 },
  'Magic Damage': { magicDamage: 10 },
  'Paralyze': { paralyze: true },
  'Electric Damage': { extraDamage: 8, magicDamage: 4 },
  'Soul Trap': { soulTrap: true },
  'Blood Scythe': {
    inflict: {
      type: 'Injury',
      chance: 0.003 // 0.3%
    },
    lifesteal: 0.15 // 15% of damage dealt
  },
};

export const ARMOR_ENCHANTMENTS = {
  'Fortify Archery': { damageBonus: 0.15 },
  'Fortify Barter': { betterPrices: 0.10 },
  'Fortify Healing Rate': { healthRegen: 1 },
  'Fortify Health': { extraHealth: 0.15 },
  'Fortify Armor': { extraArmor: 8 },
  'Fortify Magic': { extraMagic: 10 },
  'Fortify Magic Regen': { magicRegen: 1 },
  'Fortify One-Handed': { damageBonus: 10 },
  'Fortify Two-Handed': { damageBonus: 15 },
  'Fortify Unarmed': { extraDamage: 25 },
  'Resist Fire': { fireResist: 0.15 },
  'Resist Ice': { iceResist: 0.15 },
  'Resist Magic': { magicResist: 0.5 },
  'Resist Poison': { poisonResist: true },
  'Resist Electric': { electricResist: 0.3 },
  'Drop Rate Boost': { dropRateBoost: 0.05 },
};

function isEnchantmentAllowed(itemType, enchantmentName) {
  const allowed = ENCHANTMENT_RULES[itemType] || [];
  return allowed.includes(enchantmentName);
}

// enchantments.js
export function getDropRateBoost(player) {
  const boostEnchant = player.enchantments?.find(e => e === 'Drop Rate Boost');
  return boostEnchant ? 0.05 : 0;
}

// TODO: Add more enchantments as needed, along with their effects and flavor texts