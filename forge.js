import { INGOT_RECIPES, RAW_RESOURCES } from './forgeResources.js';

export function upgradeEquipmentItem(player, itemName) {
  const item = player.equipment?.[itemName];
  if (!item) return console.log("Item not equipped.");

  const cost = getUpgradeCost(item.level || 1);
  if (player.ingots < cost) return console.log(`You need ${cost} ingots to upgrade ${itemName}.`);

  player.ingots -= cost;
  item.level = (item.level || 1) + 1;
  item.power = (item.power || 0) + Math.floor(2 + item.level * 1.5);
  item.forgeLocked = true;

  console.log(`${itemName} upgraded to level ${item.level}!`);
}

export function getUpgradeCost(level) {
  return Math.floor((level ** 1.5) + level); // Can mirror relic scaling or be tuned differently
}

export function addIngots(player, amount) {
  player.ingots = (player.ingots || 0) + amount;
  console.log(`+${amount} ingot${amount > 1 ? 's' : ''} added.`);
}

export function craftIngot(player, resourceName, amount = 1) {
  if (!player.resources || !player.resources[resourceName]) {
    return console.log(`You don’t own any ${resourceName}.`);
  }

  const recipe = INGOT_RECIPES[resourceName];
  const raw = RAW_RESOURCES[resourceName];

  if (!recipe || !raw) return console.log(`❌ ${resourceName} cannot be refined into an ingot.`);

  const available = player.resources[resourceName];
  if (available < amount) return console.log(`You only have ${available} ${resourceName}.`);

  const totalYield = amount * raw.forgeYield;
  player.resources[resourceName] -= amount;
  player.ingotsByType ??= {};
  player.ingotsByType[recipe.ingotType] = (player.ingotsByType[recipe.ingotType] || 0) + totalYield;

  console.log(`🔨 Forged ${totalYield} ${recipe.ingotType}${totalYield > 1 ? 's' : ''} from ${amount} ${resourceName}.`);
}

// 🔧 Utility functions
export function canUseIngot(item, ingotType) {
  return INGOT_RECIPES[item.requiredResource]?.ingotType === ingotType;
}

export function isResourceValidForGear(resource, gearMaterial) {
  return INGOT_RECIPES[resource]?.usedOn.includes(gearMaterial);
}