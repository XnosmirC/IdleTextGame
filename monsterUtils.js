

export function getEnemyHealthMultiplier(player) {
  const stageFactor = 1 + (player.stage * 0.1);
  return stageFactor;
}

export function getEnemyAttackMultiplier(player) {
  const stageFactor = 1 + (player.stage * 0.08);
  return stageFactor;
}