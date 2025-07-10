export const ELEMENTS = [
  'fire', 'ice', 'electric', 'earth',
  'spirit', 'darkness', 'poison', 'rage', 'neutral',
];

export const DOT_VALUES = {
  common: 1,
  uncommon: 2,
  rare: 3,
  epic: 3,
  legendary: 3,
  unique: 3,
};

export const RARITY_MULTIPLIERS = {
  common: 1,
  uncommon: 1.25,
  rare: 1.75,
  epic: 2.25,
  legendary: 2.75,
  unique: 3.5,
};

export const difficultyMultiplier = 1.1; // Enemies get 10% stronger per loop
export const rewardMultiplier = 1.75;    // Rewards increase by 75%

export const smallMonsterElements = [...ELEMENTS];
export const mediumMonsterElements = [...ELEMENTS];

export const CRYSTAL_REWARD = {
  perBoss: 0.05,
  perGold: 500000
};