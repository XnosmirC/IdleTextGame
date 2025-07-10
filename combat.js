import { calculateDamage } from './combatUtils.js';
import { difficultyMultiplier, rewardMultiplier } from './constants.js';
import { getDropRateBoost } from './enchantments.js';
import { getEnemyHealthMultiplier, getEnemyAttackMultiplier } from './monsterUtils.js';
import { ENCHANTMENTS } from './enchantments.js';
import { STATUS_EFFECTS } from './statusEffects.js'; // Bleeding defined here

const MONSTER_CRIT_STATS = {
  small: { critChance: 0.00, critMultiplier: 1.5 },
  medium: { critChance: 0.10, critMultiplier: 1.6 },
  boss: { critChance: 0.15, critMultiplier: 1.75 }
};

export function generateBoss(bossesSlain, player) {
  const elements = ['fire', 'ice', 'electric', 'spirit', 'rage', 'poison', 'darkness', 'neutral'];
  const bossElement = elements[Math.floor(Math.random() * elements.length)];

  const health = 5000 * (difficultyMultiplier ** bossesSlain) * getEnemyHealthMultiplier(player);
  const attack = 350 * (difficultyMultiplier ** bossesSlain) * getEnemyAttackMultiplier(player);

  return {
    element: bossElement,
    health,
    attack,
    critChance: MONSTER_CRIT_STATS.boss.critChance,
    critMultiplier: MONSTER_CRIT_STATS.boss.critMultiplier,
    name: `Stage ${player.stage} Boss of ${bossElement.toUpperCase()}`,
    status: null,
    level: bossesSlain + 1
  };
}

export function startBossFight(player) {
  const boss = generateBoss(player.bossesSlain, player);

  player.bossAttempts += 1;
  if (player.bossAttempts >= 10 && !player.pityBuff && !player.hasUsedPityBuff) {
    player.applyPityBuff();
    console.log("🛡️ Pity Buff activated!");
  }

  // --- Player Attacks ---
  let damage = calculateDamage({
    baseDamage: player.stats.attack,
    userElement: player.stats.element,
    monsterElement: boss.element,
    weaponRarity: 'common',
    critChance: player.stats.critChance || 0,
    critMultiplier: player.stats.critMultiplier || 1.5
  });

  // Apply Blood Scythe effects
  const hasScythe = player.enchantments?.includes('Blood Scythe');
  if (hasScythe) {
    const { inflict, lifesteal } = ENCHANTMENTS['Blood Scythe'];

    if (Math.random() < inflict.chance) {
      boss.status = {
        type: 'Bleeding',
        turnsRemaining: STATUS_EFFECTS.Bleeding.duration
      };
      console.log(`🩸 ${boss.name} is inflicted with Bleeding!`);
    }

    const healAmount = Math.floor(damage * lifesteal);
    player.health = Math.min(player.health + healAmount, player.maxHealth);
    console.log(`🧛 You siphon ${healAmount} HP from the attack.`);
  }

  // Apply weakness-based extra damage
  if (player.activeEffects?.extra_damage_multiplier) {
    damage *= player.activeEffects.extra_damage_multiplier;
  }

  boss.health -= damage;
  console.log(`You hit the boss for ${Math.floor(damage)} damage!`);

  // Bleeding status tick
  if (boss.status?.type === 'Bleeding') {
    const bleedDamage = STATUS_EFFECTS.Bleeding.damagePerTurn(boss.level);
    boss.health -= bleedDamage;
    boss.status.turnsRemaining--;

    console.log(`☠️ ${boss.name} bleeds for ${bleedDamage} damage.`);

    if (boss.status.turnsRemaining <= 0) {
      boss.status = null;
      console.log(`${boss.name} stops bleeding.`);
    }
  }

  if (boss.health <= 0) {
    player.bossesSlain++;
    const reward = Math.round(100 * (rewardMultiplier ** player.bossesSlain));
    player.gold += reward;
    console.log(`🎉 You defeated the boss! You earned ${reward} gold.`);
    if (player.pityBuff) player.removePityBuff();
    player.bossAttempts = 0;
    return;
  }

  // --- Boss Attacks ---
  const bossDamage = calculateDamage({
    baseDamage: boss.attack,
    userElement: boss.element,
    monsterElement: player.stats.element,
    weaponRarity: 'common',
    critChance: boss.critChance,
    critMultiplier: boss.critMultiplier
  });

  player.health -= bossDamage;
  if (player.health <= 0) {
    console.log("💀 You were defeated by the boss...");
    console.log("Retreating to the previous stage to recover and grind. Earn gold, level up, and return stronger!");
    player.stage = Math.max(1, player.stage - 1);
    player.health = 100;
  } else {
    console.log(`Boss hits you for ${Math.floor(bossDamage)} damage. Your HP: ${Math.floor(player.health)}`);
  }

  if (player.pityBuff) player.removePityBuff();
}