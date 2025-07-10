import { spawnBoss } from './boss.js';
import { smallMonsterElements } from './constants.js'; // define globally if used in multiple files

let smallMonsterKills = 0;
let mediumMonsterKills = 0;

export function killSmallMonster(player) {
  smallMonsterKills++;
  player.earnGold(10);
  console.log(`A small monster has been killed! You earned 10 gold. Total: ${player.gold}`);
  checkBossSpawn();
}

export function killMediumMonster(player) {
  mediumMonsterKills++;
  player.earnGold(30);
  console.log(`A medium monster has been killed! You earned 30 gold. Total: ${player.gold}`);
  checkBossSpawn();
}

function checkBossSpawn() {
  const totalKills = smallMonsterKills + mediumMonsterKills;
  if (totalKills >= 25) {
    smallMonsterKills = 0;
    mediumMonsterKills = 0;
    spawnBoss();
  }
}

export function spawnSmallMonster(element) {
  console.log(`A small monster with element ${element} has spawned!`);
}

export function spawnMediumMonster(element) {
  console.log(`A medium monster with element ${element} has spawned!`);
}

export function spawnMonster(type) {
  const element = smallMonsterElements[Math.floor(Math.random() * smallMonsterElements.length)];
  if (type === 'small') spawnSmallMonster(element);
  else if (type === 'medium') spawnMediumMonster(element);
}