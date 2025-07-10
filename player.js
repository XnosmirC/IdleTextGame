import { Inventory } from './inventory.js';

export const baseUserStats = {
  health: 100,
  magicka: 100,
  attack: 5,
  defense: 5,
  element: null,
  gold: 0,
};

export class Player {
  constructor(id = 'player') {
    this.id = id;
    this.points = 0;
    this.gold = 0;
    this.health = 100;
    this.stats = { ...baseUserStats };
    this._originalStats = null;

    // Progress & state
    this.bossesSlain = 0;
    this.smallMonstersDefeated = 0;
    this.mediumMonstersDefeated = 0;
    this.hasUsedPityBuff = false;
    this.pityBuff = false;

    // Inventory & combat
    this.inventory = new Inventory();
    this.potionInventory = new Inventory();
    this.equipment = {};
    this.spells = {};
    this.enchantments = [];
    this.hasPurchasedFromShop = false;

    // Consumable tracking
    this.consumableUses = {};
    const types = ['Honey', 'Jelly', 'Ambrosia'];
    const colors = ['Red', 'Green', 'Blue', 'White', 'Black', 'Yellow', 'Orange', 'Purple', 'Clear'];
    const drinks = [
      'Pixie Cider', 'Asgardian Punch', 'Party Popper Champagne', "Dragon's Breath Mead",
      'Spiced Wine', "Juniper's Brew", 'Undercroft Ale', 'Iced Lager', 'Orcish Rotgut Ale'
    ];

    for (let drink of drinks) this.consumableUses[drink] = 0;
    for (let type of types) {
      for (let color of colors) {
        this.consumableUses[`${color} ${type}`] = 0;
      }
    }
  }

  earnGold(amount) {
    this.gold += amount;
  }

  defeatSmallMonster() {
    this.smallMonstersDefeated++;
    const gold = Math.floor(5 + this.stage * 1.5);
    this.earnGold(gold);
  }

  defeatMediumMonster() {
    this.mediumMonstersDefeated++;
    const gold = Math.floor(15 + this.stage * 2.75);
    this.earnGold(gold);
  }

  applyPityBuff() {
    if (!this.pityBuff && !this.hasUsedPityBuff) {
      this._originalStats = { ...this.stats };
      this.stats.attack *= 1.5;
      this.stats.defense *= 1.5;
      this.pityBuff = true;
      this.hasUsedPityBuff = true;
      console.log("You've received a temporary pity buff.");
    }
  }

  removePityBuff() {
    if (this.pityBuff && this._originalStats) {
      this.stats.attack = this._originalStats.attack;
      this.stats.defense = this._originalStats.defense;
      this.pityBuff = false;
      this._originalStats = null;
      console.log("Your pity buff has worn off. Your stats have returned to normal.");
    }
  }
}