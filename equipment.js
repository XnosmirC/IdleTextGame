export function equipItem(player, itemName) {
  const item = player.equipment[itemName];
  if (!item) {
    console.log(`You don't have ${itemName} in your equipment.`);
    return;
  }

  const isAccessory = ['Broach', 'Bracelet'].includes(itemName);
  const compatibleArmor = ['Cloth', 'Leather', 'Cloak', 'Robes'];
  const wearingCompatible = compatibleArmor.some(armor => player.equipment[armor]);

  if (isAccessory && !wearingCompatible) {
    console.log(`You can't equip ${itemName} without wearing ${compatibleArmor.join(', ')}.`);
    return;
  }

  player.stats.element = item.element || 'neutral';
  if (item.attackBonus) player.stats.attack += item.attackBonus;
  if (item.defenseBonus) player.stats.defense += item.defenseBonus;

  if (item.enchantment) {
    applyEnchantment(player, item.enchantment);
  }

  console.log(`You've equipped ${itemName} with ${player.stats.element} element. Bonuses applied.`);
}

player.equipment = {
  head: null,
  chest: null,
  leggings: null,
  gauntlets: null,
  boots: null,
  weapon: null,
  offhand: null,
  shield: null,
  accessory1: null,
  accessory2: null,
};

