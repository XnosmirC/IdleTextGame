import { baseUserStats } from './player.js';
import { WEAPON_ENCHANTMENTS, ARMOR_ENCHANTMENTS } from './enchantments.js';



// 🧨 Boss Lifecycle
export function spawnBoss() {
  console.log('A boss has spawned!');
}

export function defeatBoss(player, smallKills, mediumKills) {
  const bonus = Math.floor(player.gold * 0.75);
  player.gold += bonus;
  const goldPerKill = player.gold / (smallKills + mediumKills + 1);
  console.log(`You defeated a boss! Earned +${bonus} gold (75% bonus). Total gold: ${player.gold}. New gold per kill: ${goldPerKill.toFixed(2)}`);
}

// 🧪 Phoenix Feather Revive Logic
export function attemptRevival(player, itemName = 'Phoenix Feather') {
  if (player.health > 0) return false;

  const hasRevive = player.inventory?.hasItem?.(itemName);
  if (!hasRevive) return false;

  player.inventory.removeItem(itemName);
  player.health = Math.floor(player.maxHealth * 0.5);
  if (player.status) delete player.status;

  console.log(`🔥 The ${itemName} activates! You return to battle with ${player.health} HP.`);
  return true;
}

// 🎁 Boss Reward System
export function checkBossRewards(player) {
  const rewards = [
    { kills: 5000000, gold: 1000, items: ['unique'] },
    { kills: 350000, gold: 750, items: ['epic', 'epic'] },
    { kills: 30000,   gold: 500, items: ['epic'] },
    { kills: 2500,    gold: 300, items: ['legendary', 'legendary'] },
    { kills: 200,     gold: 250, items: ['legendary'] },
    { kills: 150,     gold: 200, items: ['legendary', 'legendary'] },
    { kills: 10,      gold: 150, items: ['rare'] },
    { kills: 5,       gold: 100, items: ['rare'] },
  ];

  const getRandom = arr => arr[Math.floor(Math.random() * arr.length)];

  const determineEnchantmentCount = (slain) => {
    if (slain >= 350_000) return { guaranteed: 3, chanceForExtra: 0.05 };
    if (slain >= 30_000)  return { guaranteed: 2, chanceForExtra: 0.01 };
    if (slain >= 200)     return { guaranteed: 1, chanceForExtra: 0.01 };
    return { guaranteed: 1, chanceForExtra: 0 };
  };

  const generateMultiEnchantedItem = (baseItem, { guaranteed, chanceForExtra }, pool) => {
    const shuffled = shuffle(pool).filter(e => isEnchantmentAllowed(baseItem.type, e.name));
    const enchantments = shuffled.slice(0, guaranteed);

    if (chanceForExtra && Math.random() < chanceForExtra && shuffled.length > guaranteed) {
      enchantments.push(shuffled[guaranteed]);
    }

    const name = generateItemName(baseItem.name, enchantments[0]); // Upgrade: combine names if needed
    return { ...baseItem, enchantments, name };
  };

  // Determine bonus
  let bonusGold = 0;
  let bonusItems = [];

  if (player.bossesSlain >= 50 && player.bossesSlain % 5 === 0) {
    bonusGold = player.stage * 50; // Example scaling
    bonusItems = ['unique', 'unique'];
  } else {
    const reward = rewards.find(r => r.kills === player.bossesSlain);
    if (reward) {
      bonusGold = reward.gold + (player.stage * 10); // stage-based kicker
      bonusItems = reward.items;
    }
  }

  // Apply rewards
  if (bonusGold > 0 && bonusItems.length > 0) {
    player.gold += bonusGold;

    const enchantmentPool = getEnchantmentPool(WEAPON_ENCHANTMENTS, ARMOR_ENCHANTMENTS);

    const dropItems = bonusItems.map(itemRarity => {
      const baseItem = getBaseItemByRarity(itemRarity);
      const enchantmentCount = determineEnchantmentCount(player.bossesSlain);
      return generateMultiEnchantedItem(baseItem, enchantmentCount, enchantmentPool);
    });

    dropItems.forEach(item => player.inventory.add(item));

    console.log(`You've slain ${player.bossesSlain} bosses! You earned a bonus of ${bonusGold} gold and the following items: ${bonusItems.join(', ')}. Total gold: ${player.gold}`);
  }
}