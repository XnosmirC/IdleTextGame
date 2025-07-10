export const RARITIES = ['common', 'uncommon', 'rare', 'epic', 'legendary', 'unique'];

export const MATERIALS = {
  'Cloth': { defense: [0, 4], canBeEnchanted: true, rarity: ['common', 'unique'] },
  'Leather': { defense: [3, 7], canBeEnchanted: true, rarity: ['common', 'rare'] },
  'Chain Mail': { defense: [3, 8], canBeEnchanted: false, rarity: ['common', 'rare'] },
  'Bone': { defense: [6, 10], canBeEnchanted: true, rarity: ['common', 'legendary'] },
  'Bronze': { defense: [8, 14], canBeEnchanted: true, rarity: ['common', 'rare'] },
  'Iron': { defense: [5, 13], canBeEnchanted: true, rarity: ['common', 'epic'] },
  'Gold': { defense: [8, 15], canBeEnchanted: true, rarity: ['common', 'epic'] },
  'Silver': { defense: [8, 15], canBeEnchanted: true, rarity: ['common', 'epic'] },
  'Steel': { defense: [9, 18], canBeEnchanted: false, rarity: ['common', 'legendary'] },
  'Ebony': { defense: [12, 20], canBeEnchanted: true, rarity: ['rare', 'unique'] },
  'Platinum': { defense: [13, 22], canBeEnchanted: true, rarity: ['epic', 'unique'] },
  'Diamond': { defense: [0, 0], canBeEnchanted: true, rarity: ['rare', 'unique'] },
  'Emerald': { defense: [0, 0], canBeEnchanted: true, rarity: ['rare', 'unique'] },
  'Quartz': { defense: [0, 0], canBeEnchanted: true, rarity: ['common', 'rare'] },
  'Ruby': { defense: [0, 0], canBeEnchanted: true, rarity: ['uncommon', 'unique'] },
  'Sapphire': { defense: [0, 0], canBeEnchanted: true, rarity: ['epic', 'unique'] },
  'Dragon Bone': { defense: [16, 25], canBeEnchanted: true, rarity: ['epic', 'unique'] },
  'Mithril': { defense: [30, 45], canBeEnchanted: true, rarity: ['unique', 'unique'] },
};

export const rarityMilestones = {
  common: 0,
  uncommon: 15,
  rare: 45,
  epic: 125,
  legendary: 250,
  unique: 550,
};

export function updateAvailableRarities(bossesSlain) {
  return Object.entries(rarityMilestones)
    .filter(([_, milestone]) => bossesSlain >= milestone)
    .map(([rarity]) => rarity);
}