const listeners = {};

export const eventBus = {
on(event, handler) {
    if (!listeners[event]) listeners[event] = [];
    listeners[event].push(handler);
},

off(event, handler) {
    if (listeners[event]) {
    listeners[event] = listeners[event].filter(h => h !== handler);
    }
},

emit(event, data) {
    if (listeners[event]) {
    listeners[event].forEach(handler => handler(data));
    }
}
};

// Example usage:
eventBus.on('playerLevelUp', ({ newLevel }) => {
    console.log(`You've reached level ${newLevel}.`);
});

eventBus.emit('playerLevelUp', { newLevel: 5 });