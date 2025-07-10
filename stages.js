export function initializeStages(player) {
  player.stage = 1;
  player.currentBoss = getBossForStage(player.stage);
}

export function advanceStage(player) {
  player.stage++;
  player.currentBoss = getBossForStage(player.stage);
}

export function retreatStage(player) {
  if (player.stage > 1) {
    player.stage--;
    player.currentBoss = getBossForStage(player.stage);
  }
}

function getBossForStage(stage) {
  const bosses = {
    1: 'Goblin King',
    2: 'Frost Maw',
    3: 'Voltarra the Stormcaller',
    4: 'The Bone Tyrant',
    5: 'Crimson Wyrm',
    6: 'Emberjaw the Molten',
    7: 'Queen Thornshade',
    8: 'The Hollow Revenant',
    9: 'Skarn of the Abyss',
    10: 'Ironhide Behemoth',
    11: 'Wailing Widow',
    12: 'The Ashen Duke',
    13: 'Zephira of the Winds',
    14: 'Gnarlroot Prime',
    15: 'The Sunken Horror',
    16: 'Xalatrix the Mindbender',
    17: 'Baneclaw, Hound of Ruin',
    18: 'The Shimmering Maw',
    19: 'Orryx, Eye of Madness',
    20: 'Dreadknight Varn',
    21: 'Eclipse Serpent',
    22: 'The Howling Matron',
    23: 'Krugor the Unyielding',
    24: 'The Gloom Sovereign',
    25: 'Thorned Juggernaut',
    26: 'Velkriss the Voidcaller',
    27: 'Molgroth, Flame Eater',
    28: 'The Silver Reaper',
    29: 'Arcanith the Forbidden',
    30: 'Brolgar, Titan of Ice',
    31: 'The Phantom King',
    32: 'Rakzom the Devourer',
    33: 'The Nameless Watcher',
    34: 'Ixora the Venom Queen',
    35: 'Cindertide Overlord',
    36: 'Thalrex the Blighted',
    37: 'The Hollowed Seer',
    38: 'Stormveil Kraken',
    39: 'Nexilith the Shattered',
    40: 'Morgarax the Ancient',
    41: 'The Dreampiercer',
    42: 'Blazebound Hydra',
    43: 'The Withering Duke',
    44: 'Velmora the Silencer',
    45: 'The Grinning Idol',
    46: 'Kraegon the Soulfire',
    47: 'Gorvokh, Doomfang',
    48: 'The Forgotten Herald',
    49: 'Xarthul, Bringer of Plagues',
    50: 'The Crimson Basilisk',
    51: 'The Drowned Baroness',
    52: 'Grizzlefang Chieftain',
    53: 'The Frostbound Warden',
    54: 'Lirathos the Moon-Eater',
    55: 'Terrormaw Alpha',
    56: 'Skelgrin the Graveforged',
    57: 'The Obsidian Oracle',
    58: 'Zulrik the Shardcaster',
    59: 'The Silent Executioner',
    60: 'Vorgrimm, Lord of Chains',
    61: 'The Thorn Queen',
    62: 'Azarith the Voidsworn',
    63: 'Brimestone Colossus',
    64: 'Nyssara the Darkhearted',
    65: 'The Star-Eater',
    66: 'Malgrim the Wretched',
    67: 'The Cursed Paladin',
    68: 'Shardjaw Leviathan',
    69: 'Drelzan of the Black Flame',
    70: 'The Time-Shattered Warden',
    71: 'Nerak, Herald of Sorrow',
    72: 'The Smiling Dread',
    73: 'Kelbor the Twisted',
    74: 'The Iron Warden',
    75: 'Scarknight Rilven',
    76: 'Flamespike the Unbound',
    77: 'Vorgrath, Doomcaller',
    78: 'Whisperthorn the Elusive',
    79: 'The Pale Juggernaut',
    80: 'Gravemaul Overseer',
    81: 'The Fanged Oracle',
    82: 'Silithra the Mirage Warden',
    83: 'Barrowshade the Vile',
    84: 'The Ember Matron',
    85: 'Harrowfang Alpha',
    86: 'The Sculptor of Agony',
    87: 'Zyrak the Faceless',
    88: 'The Hollow Flame',
    89: 'Drekar, Abyssal Tyrant',
    90: 'The Frostvein Horror',
    91: 'Molthrax the Infernal',
    92: 'Elderspike the Timeless',
    93: 'The Blight Druid',
    94: 'Korvyn, Breaker of Realms',
    95: 'The Unseen Sovereign',
    96: 'Shriekthorn Emissary',
    97: 'Thalgor the Reborn',
    98: 'The Wandering King',
    99: 'Azrak, Thorned Nightmare',
    100: 'The Lost Flame'
  };

  return bosses[stage] || '???';
}