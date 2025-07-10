function handleBuy() {
  const itemToBuy = prompt("Enter the name of the item you want to buy:");
  buy(player, itemToBuy);
}

function handleEquip() {
  const itemName = prompt("Enter the item to equip:");
  equipItem(player, itemName);
}

function handleUnequip() {
  const itemName = prompt("Enter the item to unequip:");
  unequipItem(player, itemName);
}

function handleSell() {
  const itemToSell = prompt("Enter the item to sell:");
  sellItem(player, itemToSell);
}

function handleGrind() {
  player.grindMode = true;
  console.log("🔁 You’ve chosen to grind this stage manually. Auto-progression paused.");
}

// Only one handleCommand exists now
function handleCommand(cmd) {
  switch (cmd.toUpperCase()) {
    case 'B': return handleBuy();
    case 'E': return handleEquip();
    case 'U': return handleUnequip();
    case 'S': return handleSell();
    case 'G': return handleGrind();
    default:
      console.log("Invalid command. Please enter B, E, U, S, or G.");
  }
}