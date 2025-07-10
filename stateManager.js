let gameState = {
    player: {
    equipment: {},
    prestige: 0,
    crystals: 0,
    },
    inventory: [],
    shop: {},
    bossesSlain: 0,
    gold: 0,
};

updateState({ relicTabUnlocked: true });

function calculateCrystalsEarned(bossesSlain, gold) {
    const base = Math.floor(bossesSlain * 0.05);            // 1 crystal per 20 bosses slain
    const goldBonus = Math.floor(gold / 5000);              // 1 crystal per 5000 gold
    return base + goldBonus;
}

export function initializeState(playerTemplate) {
    gameState.player = { ...playerTemplate };
}

export function getState() {
    return structuredClone(gameState);
}

export function updateState(partial) {
    gameState = { ...gameState, ...partial };
}

export function saveStateToLocalStorage() {
    localStorage.setItem('gameState', JSON.stringify(gameState));
}

export function loadStateFromLocalStorage() {
    const saved = localStorage.getItem('gameState');
    if (saved) gameState = JSON.parse(saved);
}

export function resetState() {
    gameState = { player: null, inventory: [], shop: {}, bossesSlain: 0, gold: 0 };
}

export function checkForgeUnlock(player) {
    if (!player.forgeUnlocked && player.bossesSlain >= 5) {
    player.forgeUnlocked = true;
    console.log("🔥 The Forge has awakened! You may now refine materials and upgrade equipment.");
    }
}