export class Inventory {
  constructor(capacity = 20) {
    this.capacity = capacity;
    this.items = [];
  }

  add(item) {
    const existing = this.items.find(i => i.name === item.name);

    if (existing && item.stackable) {
      if (existing.quantity < item.stackLimit) {
        existing.quantity++;
        console.log(`Stacked 1x ${item.name} (${existing.quantity}/${item.stackLimit})`);
      } else {
        console.log(`${item.name} stack is full.`);
      }
      return;
    }

    if (this.items.length < this.capacity) {
      item.quantity = 1;
      this.items.push(item);
      console.log(`You've added ${item.name} to your inventory.`);
    } else {
      console.log("Your inventory is full.");
    }
  }
}