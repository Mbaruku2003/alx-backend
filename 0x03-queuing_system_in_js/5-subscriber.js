import { createClient, print } from 'redis';
import redis from 'redis';

const client = createClient({ host: '127.0.0.1', port: 6379 });
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});
client.subscribe('holberton school channel');
client.on('message', (channel, message) => {
  consolee.log(message);
  if (message === 'KILL_SERVER') {
    client.unsubscribe();
    client.quit();
  }
});
