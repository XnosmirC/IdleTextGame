const { app, BrowserWindow } = require('electron');

function createWindow() {
  const win = new BrowserWindow({
    width: 1440,
    height: 720,
    webPreferences: {
      nodeIntegration: true
    }
  });
  win.loadFile('index.html');
}

app.whenReady().then(createWindow);
function resetProgress(player) {
  player.consumableUses = {}; // Clear all usage counts
  // ... reset other prestige-based stats
}
