import { CRYSTAL_REWARD } from './constants.js';
import { resetState, defaultPlayerState } from './stateManager.js';

export function calculateCrystalsEarned(bossesSlain, gold) {
  const base = Math.floor(bossesSlain * CRYSTAL_REWARD.perBoss);
  const goldBonus = Math.floor(gold / CRYSTAL_REWARD.perGold);
  return base + goldBonus;
}

// Step 1: Warn the player and flag pending prestige
export function confirmPrestige(player) {
  const earned = calculateCrystalsEarned(player.bossesSlain, player.gold);

  console.log("⚠️ Are you sure you want to transcend?");
  console.log("You will lose:");
  console.log(" - Gold, inventory, unequipped gear, and stage progress");
  console.log("You will keep:");
  console.log(" - Crystal Items, Ingots, Forge-upgraded equipment");
  console.log(`You will gain: +${earned} Elemental Crystals`);
  console.log("Type `confirmPrestigeFinal(player)` to proceed.");

  player._pendingPrestige = true;
}

// Step 2: Finalize the prestige and apply changes
export function confirmPrestigeFinal(player) {
  if (!player._pendingPrestige) {
    console.log("💬 Please confirm prestige first using `confirmPrestige(player)`.");
    return;
  }
  delete player._pendingPrestige;

  const earned = calculateCrystalsEarned(player.bossesSlain, player.gold);

  const retainedEquipment = {};
  for (let slot in player.equipment) {
    const item = player.equipment[slot];
    if (item?.forgeLocked) retainedEquipment[slot] = item;
  }

  const newPlayer = {
    ...defaultPlayerState,
    crystals: player.crystals + earned,
    ingots: player.ingots,
    prestige: player.prestige + 1,
    equipment: retainedEquipment,
    crystalItems: player.crystalItems,
  };

  if (Object.keys(retainedEquipment).length > 0) {
    console.log("🔒 The following gear resisted the reset:");
    Object.keys(retainedEquipment).forEach(slot =>
      console.log(` - ${slot}: ${retainedEquipment[slot].name || 'Unnamed Item'}`));
  }

  console.log(`✨ You transcended! You've gained ${earned} Elemental Crystals. Total crystals: ${newPlayer.crystals}`);

  resetState(); // Optional: Reset entire game state except player
  return newPlayer;
}