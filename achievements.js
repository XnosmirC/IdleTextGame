import { log } from './log.js';
import { audio } from './audio.js';

export function checkAchievements(player) {
  for (const [name, def] of Object.entries(ACHIEVEMENT_DEFINITIONS)) {
    if (def.condition(player) && !achievements.includes(name)) {
      achievements.push(name);
      log('achievement', `${def.icon} Achievement unlocked: ${name} – ${def.description}`);
      audio.play('achievement-ding');
    }
  }
}

export const achievements = [];

export const ACHIEVEMENT_DEFINITIONS = {
  // 🧟 Boss Kill Achievements
  'The first of many': {
    description: 'Defeat your first boss.',
    icon: '⚔️',
    condition: p => p.bossesSlain >= 1,
    progress: p => Math.min(p.bossesSlain / 1, 1)
  },
  'Boss Slayer': {
    description: 'Defeat 10 bosses.',
    icon: '⚔️',
    condition: p => p.bossesSlain >= 10,
    progress: p => Math.min(p.bossesSlain / 10, 1)
  },
  'Boss Conqueror': {
    description: 'Defeat 50 bosses.',
    icon: '⚔️',
    condition: p => p.bossesSlain >= 50,
    progress: p => Math.min(p.bossesSlain / 50, 1)
  },
  'Boss Annihilator': {
    description: 'Defeat 200 bosses.',
    icon: '⚔️',
    condition: p => p.bossesSlain >= 200,
    progress: p => Math.min(p.bossesSlain / 200, 1)
  },
  'Boss Obliterator': {
    description: 'Defeat 500 bosses.',
    icon: '⚔️',
    condition: p => p.bossesSlain >= 500,
    progress: p => Math.min(p.bossesSlain / 500, 1)
  },
  'Boss Eradicator': {
    description: 'Defeat 1,000 bosses.',
    icon: '⚔️',
    condition: p => p.bossesSlain >= 1000,
    progress: p => Math.min(p.bossesSlain / 1000, 1)
  },
  'Boss Exterminator': {
    description: 'Defeat 25,000 bosses.',
    icon: '⚔️',
    condition: p => p.bossesSlain >= 25000,
    progress: p => Math.min(p.bossesSlain / 25000, 1)
  },
  'Boss Devastator': {
    description: 'Defeat 500,000 bosses.',
    icon: '⚔️',
    condition: p => p.bossesSlain >= 500000,
    progress: p => Math.min(p.bossesSlain / 500000, 1)
  },
  'Boss Emulcifier': {
    description: 'Defeat 1,000,000 bosses.',
    icon: '⚔️',
    condition: p => p.bossesSlain >= 1000000,
    progress: p => Math.min(p.bossesSlain / 1000000, 1)
  },

  // 🔁 Prestige Achievements
  'Is this Real Life?': {
    description: 'Complete your first prestige.',
    icon: '🔁',
    condition: p => p.prestige >= 1,
    progress: p => Math.min(p.prestige / 1, 1)
  },
  'Or Just Fantasy?': {
    description: 'Complete 50 prestiges.',
    icon: '🔁',
    condition: p => p.prestige >= 50,
    progress: p => Math.min(p.prestige / 50, 1)
  },
  'Caught in a Landslide': {
    description: 'Complete 1,000 prestiges.',
    icon: '🔁',
    condition: p => p.prestige >= 1000,
    progress: p => Math.min(p.prestige / 1000, 1)
  },
  'No Escape from Reality': {
    description: 'Complete 25,000 prestiges.',
    icon: '🔁',
    condition: p => p.prestige >= 25000,
    progress: p => Math.min(p.prestige / 25000, 1)
  },
  'All you are': {
    description: 'Complete 500,000 prestiges.',
    icon: '🔁',
    condition: p => p.prestige >= 500000,
    progress: p => Math.min(p.prestige / 500000, 1)
  },
  'Is dust in the wind': {
    description: 'Complete 1,000,000 prestiges.',
    icon: '🔁',
    condition: p => p.prestige >= 1000000,
    progress: p => Math.min(p.prestige / 1000000, 1)
  },

  // 💰 Gold Achievements
  'One measly coin': {
    description: 'Collect your first gold.',
    icon: '🪙',
    condition: p => p.gold >= 1,
    progress: p => Math.min(p.gold / 1, 1)
  },
  'Gleamy, Shiny Coin': {
    description: 'Collect 500 gold.',
    icon: '🪙',
    condition: p => p.gold >= 500,
    progress: p => Math.min(p.gold / 500, 1)
  },
  'Gold Digger': {
    description: 'Collect 1,000 gold.',
    icon: '🪙',
    condition: p => p.gold >= 1000,
    progress: p => Math.min(p.gold / 1000, 1)
  },
  'Gold Rush': {
    description: 'Collect 50,000 gold.',
    icon: '🪙',
    condition: p => p.gold >= 50000,
    progress: p => Math.min(p.gold / 50000, 1)
  },
  'Gold Fever': {
    description: 'Collect 1,000,000 gold.',
    icon: '🪙',
    condition: p => p.gold >= 1000000,
    progress: p => Math.min(p.gold / 1000000, 1)
  },
  'Gold is Power': {
    description: 'Collect 1,000,000,000 gold.',
    icon: '🪙',
    condition: p => p.gold >= 1000000000,
    progress: p => Math.min(p.gold / 1000000000, 1)
  },

  // 🛍️ Shop Purchase Achievements
  'We\'ve had one purchase, yes.': {
    description: 'Buy your first item from the shop.',
    icon: '🛒',
    condition: p => p.shopPurchases >= 1,
    progress: p => Math.min(p.shopPurchases / 1, 1)
  },
  'But what about Second Purchase?': {
    description: 'Buy your second item from the shop.',
    icon: '🛍️',
    condition: p => p.shopPurchases >= 2,
    progress: p => Math.min(p.shopPurchases / 2, 1)
  },
  'Elevenses': {
    description: 'Buy 11 items from the shop.',
    icon: '🍽️',
    condition: p => p.shopPurchases >= 11,
    progress: p => Math.min(p.shopPurchases / 11, 1)
  },
  'Afternoon Tea': {
    description: 'Buy 100 items from the shop.',
    icon: '🍵',
    condition: p => p.shopPurchases >= 100,
    progress: p => Math.min(p.shopPurchases / 100, 1)
  },
  'Dinner': {
    description: 'Buy 1,000 items from the shop.',
    icon: '🍲',
    condition: p => p.shopPurchases >= 1000,
    progress: p => Math.min(p.shopPurchases / 1000, 1)
  },
  'Supper': {
    description: 'Buy 10,000 items from the shop.',
    icon: '🍽️',
    condition: p => p.shopPurchases >= 10000,
    progress: p => Math.min(p.shopPurchases / 10000, 1)
  },
  'Should have just bought the store...': {
    description: 'Buy 100,000 items from the shop.',
    icon: '🏬',
    condition: p => p.shopPurchases >= 100000,
    progress: p => Math.min(p.shopPurchases / 100000, 1)
  },
  'Shopkeeper can retire now': {
    description: 'Buy 1,000,000 items from the shop.',
    icon: '💼',
    condition: p => p.shopPurchases >= 1000000,
    progress: p => Math.min(p.shopPurchases / 1000000, 1)
  }
};