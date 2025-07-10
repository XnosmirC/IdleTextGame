import { ACHIEVEMENT_DEFINITIONS } from './achievements.js';

export function pinAchievement(player, name) {
  if (player.pinnedAchievements.includes(name)) return;
  if (player.pinnedAchievements.length >= 3) {
    console.log('📌 You can only pin up to 3 achievements.');
    return;
  }
  player.pinnedAchievements.push(name);
  console.log(`📌 Pinned: ${name}`);
}

export function unpinAchievement(player, name) {
  player.pinnedAchievements = player.pinnedAchievements.filter(a => a !== name);
  console.log(`❌ Unpinned: ${name}`);
}

export function isPinned(player, name) {
    return player.pinnedAchievements.includes(name);
  }

export function getPinnedAchievements(player) {
    return player.pinnedAchievements
      .filter(name => ACHIEVEMENT_DEFINITIONS[name])
      .map(name => ({
        name,
        ...ACHIEVEMENT_DEFINITIONS[name]
      }));
  }

export function getClosestAchievements(player, count = 3) {
  const locked = Object.entries(ACHIEVEMENT_DEFINITIONS)
    .filter(([name]) => !player.achievements.includes(name));

  const scored = locked.map(([name, def]) => {
    const progress = def.progress(player);
    return { name, ...def, progress };
  });

  return scored
    .sort((a, b) => b.progress - a.progress)
    .slice(0, count);
}