export function renderShop(shop) {
    console.clear();
    console.log('🛒 Current Shop Inventory:\n');
    Object.entries(shop).forEach(([itemName, item]) => {
    console.log(`${itemName} — ${item.price} gold — ${item.rarity} ${item.material} — ${item.element}`);
    });
}

export function renderPlayerStats(player) {
    console.log('\n🧍 Player Stats:');
    console.log(`Health: ${player.health}`);
    console.log(`Gold: ${player.gold}`);
    console.log(`Bosses Slain: ${player.bossesSlain}`);
    // Add more as needed
}

export function renderInventory(inventory) {
    console.log('\n🎒 Inventory:');
    inventory.forEach(item => console.log(`${item.name || 'Unnamed'} — ${item.rarity || 'common'}`));
}

export function showMessage(message) {
    console.log(`\n💬 ${message}`);
}