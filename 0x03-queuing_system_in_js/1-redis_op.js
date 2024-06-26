import redis from 'redis';

// Connect to the Redis server
const client = redis.createClient();

// Log connection status
client.on('connect', () => {
    console.log('Redis client connected to the server');
});

client.on('error', (err) => {
    console.error(`Redis client not connected to the server: ${err.message}`);
});
