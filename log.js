export function log(type, message) {
  const prefix = {
    combat: '⚔️',
    system: '🛠️',
    achievement: '🏆',
    loot: '💰',
  }[type] || '📘';

  console.log(`${prefix} ${message}`);
}