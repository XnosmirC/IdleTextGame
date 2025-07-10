export function play(soundName) {
  // You could map soundName to audio files later
  console.log(`🔉 SFX: ${soundName}`);
}

const sounds = {
  'achievement-ding': new Audio('sfx/achievement.mp3'),
  'monster-hit': new Audio('sfx/hit.mp3'),
  // etc.
};
