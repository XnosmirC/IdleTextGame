import { DOT_VALUES } from './constants.js';

// Elemental strength and weakness relationships
const strengths = {
  fire: 'ice',
  ice: 'electric',
  electric: 'earth',
  earth: 'fire',
  spirit: 'darkness',
  darkness: 'spirit',
  poison: 'rage',
  rage: 'poison',
};

const weaknesses = {
  fire: 'earth',
  ice: 'fire',
  electric: 'ice',
  earth: 'electric',
  spirit: 'darkness',
  darkness: 'spirit',
  poison: 'rage',
  rage: 'poison',
};

export function isStrongAgainst(userElement, targetElement) {
  return strengths[userElement] === targetElement;
}

export function isWeakAgainst(userElement, targetElement) {
  return weaknesses[userElement] === targetElement;
}
export function isResistantTo(monsterElement, userElement) {
  // Could define a 'resistances' map later
  return false;
}

export function calculateDamage({
  baseDamage = 0,
  weaponDamage = 0,
  enchantmentBonus = 0,
  itemBonus = 0,
  monsterElement = null,
  userElement = null,
  monsterDefense = 0,
  weaponRarity = 'common',
  critChance = 0,
  critMultiplier = 1.5
}) {
  let attack = baseDamage + weaponDamage + enchantmentBonus + itemBonus;

  const didCrit = Math.random() < critChance;
  if (didCrit) {
    attack *= critMultiplier; // 💥 fixed reference from 'total' to 'attack'
  }

  if (isStrongAgainst(userElement, monsterElement)) {
    attack *= 2;
  } else if (isWeakAgainst(userElement, monsterElement)) {
    attack *= 0.5;
  }

  // Apply poison DoT if applicable
  if (userElement === 'poison' && DOT_VALUES[weaponRarity]) {
    attack += DOT_VALUES[weaponRarity];
  }

  attack -= monsterDefense;
  attack = Math.max(1, attack); // Prevent negative damage

  return attack;
}
