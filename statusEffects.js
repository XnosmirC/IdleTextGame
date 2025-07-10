export const STATUS_EFFECTS = {
  Bleeding: {
    category: 'debuff',
    duration: 10,
    damagePerTurn: (lvl) => Math.floor(lvl * 1.5)
  },
  Poison: {
    category: 'debuff',
    duration: 5,
    damagePerTurn: (lvl) => lvl * 2
  },
  Confusion: {
    category: 'debuff',
    duration: 3,
    effect: 'missChance'
  },
  BoneBreak: {
    category: 'injury',
    duration: 15,
    effect: {
      movementSpeedMultiplier: 0.5,
      attackSpeedMultiplier: 0.75
    },
    removableBy: null
  },
  Aura: {
    category: 'buff',
    duration: 2,
    effect: 'blockFirstHit'
  }
};