export const STAGE_RESOURCES = {
  'Ashen Fields':      ['Iron Shard'],
  'Obsidian Bluffs':   ['Obsidian Chunk', 'Iron Shard'],
  'Hollow Depths':     ['Soul Alloy'],
  'Celestial Cradle':  ['Stardust Ore'],
  'Eclipse Citadel':   ['Ancient Core'],
  'Molten Ravine':     ['Cinder Fragment'],
  'Frozen Wastes':     ['Frost Crystal'],
  'Verdant Gloom':     ['Sapstone', 'Poison Bloom'],
  'Shattered Spires':  ['Rift Glass'],
  'Twilight Bastion':  ['Gloomsteel Ingot'],
  'Sunken Reliquary':  ['Coral Dust', 'Ancient Fossil'],
  'Thundering Steps':  ['Skyshard'],
  'Gravecoil Hollow':  ['Bone Ash'],
  'Luminous Fen':      ['Radiant Moss'],
  'Blightrot Garden':  ['Decay Pod', 'Toxic Resin'],
  'Stormvault Peak':   ['Voltaic Core']
};


export const DROP_CHANCES = {
  small: {
    'Iron Shard': 0.05,
    'Obsidian Chunk': 0.025,
    'Frost Crystal': 0.02,
    'Sapstone': 0.02,
    'Bone Ash': 0.015,
    'Poison Bloom': 0.015,
    'Radiant Moss': 0.01
  },
  medium: {
    'Iron Shard': 0.08,
    'Obsidian Chunk': 0.05,
    'Frost Crystal': 0.035,
    'Sapstone': 0.035,
    'Bone Ash': 0.03,
    'Poison Bloom': 0.03,
    'Cinder Fragment': 0.02,
    'Decay Pod': 0.02,
    'Toxic Resin': 0.015,
    'Coral Dust': 0.015,
    'Skyshard': 0.01,
    'Radiant Moss': 0.01
  },
  boss: {
    'Iron Shard': 0.08,           // neutral
    'Obsidian Chunk': 0.06,       // earth
    'Soul Alloy': 0.05,           // spirit
    'Stardust Ore': 0.04,         // electric
    'Ancient Core': 0.03,         // darkness
    'Cinder Fragment': 0.03,      // fire
    'Frost Crystal': 0.03,        // ice
    'Poison Bloom': 0.03,         // poison
    'Rift Glass': 0.025,          // rage
    'Radiant Moss': 0.02,         // spirit support
    'Decay Pod': 0.02,
    'Toxic Resin': 0.02,
    'Gloomsteel Ingot': 0.015,
    'Skyshard': 0.015,
    'Coral Dust': 0.01,
    'Ancient Fossil': 0.01,
    'Sapstone': 0.01,
    'Bone Ash': 0.01,
    'Voltaic Core': 0.01
  }
};

export const RAW_RESOURCES = {
  'Iron Shard':        { rarity: 'common', tier: 1, forgeYield: 1 },
  'Silver Chunk':      { rarity: 'uncommon', tier: 2, forgeYield: 2 },
  'Soul Alloy':        { rarity: 'rare', tier: 3, forgeYield: 4 },
  'Raw Gold Ore':      { rarity: 'epic', tier: 4, forgeYield: 6 },
  'Ancient Core':      { rarity: 'legendary', tier: 5, forgeYield: 10 },
  'Cinder Fragment':   { rarity: 'rare', tier: 3, forgeYield: 3 },
  'Frost Crystal':     { rarity: 'rare', tier: 3, forgeYield: 3 },
  'Sapstone':          { rarity: 'uncommon', tier: 2, forgeYield: 2 },
//  'Poison Leaf':       { rarity: 'uncommon', tier: 2, forgeYield: 2 },
  'Rift Glass':        { rarity: 'epic', tier: 4, forgeYield: 5 },
  'Gloomsteel Ingot':  { rarity: 'legendary', tier: 5, forgeYield: 8 },
  'Patina Dust':        { rarity: 'rare', tier: 3, forgeYield: 3 },
  'Ancient Fossil':    { rarity: 'epic', tier: 4, forgeYield: 6 },
  'Skyshard':          { rarity: 'epic', tier: 4, forgeYield: 5 },
  'Bone Ash':          { rarity: 'uncommon', tier: 2, forgeYield: 1 },
  'Radiant Moss':      { rarity: 'rare', tier: 3, forgeYield: 2 },
  'Damp Wool':         { rarity: 'rare', tier: 3, forgeYield: 2 },
  'Monster Flesh':       { rarity: 'rare', tier: 3, forgeYield: 3 },
//  'Voltaic Core':      { rarity: 'legendary', tier: 5, forgeYield: 10 }
};

export function refineMaterial(resourceName) {
  const resource = RAW_RESOURCES[resourceName];
  return resource ? resource.forgeYield : 0;
}

export const INGOT_RECIPES = {
  'Ancient Core':        { ingotType: 'Ebony Ingot', usedOn: ['Ebony'] },
  'Ancient Fossil':      { ingotType: 'Dragonbone Ingot', usedOn: ['Dragon Bone'] },
  'Iron Shard':          { ingotType: 'Iron Ingot', usedOn: ['Iron'] },
  'Rift Glass':          { ingotType: 'Rift Glass', usedOn: ['Quartz'] },
  'Soul Alloy':          { ingotType: 'Spirit Glass', usedOn: ['Diamond'] },
  'Gloomsteel Ingot':    { ingotType: 'Gloomsteel Ingot', usedOn: ['Steel'] },
  'Bone Ash':		 { ingotType: 'Charred Bone', usedOn: ['Bone'] },
  'Sapstone': 		 { ingotType: 'River Sap Glass', usedOn: ['Sapphire']},
  'Frost Crystal':	 { ingotType: 'Frosty Ingot', usedOn: ['Platinum']},
  'Skyshard':		 { ingotType: 'Skyshard Ingot', usedOn: ['Mithril']},
  'Cinder Fragment':	 { ingotType: 'Cinder Glass', usedOn: ['Ruby']},
  'Radiant Moss':	 { ingotType: 'Moss Glass', usedOn: ['Emerald']},
  'Silver Chunk':	 { ingotType: 'Silver Ingot', usedOn: ['Silver']},
  'Raw Gold Ore':	 { ingotType: 'Gold Ingot', usedOn: ['Gold']},
  'Damp Wool':		 { ingotType: 'Fluffy Wool', usedOn: ['Cloth']},
  'Monster Flesh':	 { ingotType: 'Tanned Hide', usedOn: ['Leather']},
  'Patina Dust':	 { ingotType: 'Bronze Ingot', usedOn: ['Bronze']},
//  '':
};