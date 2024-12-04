import { createClient, print } from 'redis';
import redis from 'redis';

const client = createClient({ host: '127.0.0.1', port: 6379 });
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});
function publishMessage(message, time) {
  setTimeout(() => {
    console.log(`About to send ${message}`);
    client.publish('holberton school channel', message);
  }, time);
}
publishMessage('Holberton student #1 starts course', 100);
publishMessage('Holberton student #2 starts course', 100);
publishMessage('KILL_SERVER', 300);
publishMessage('Holberton student #3 starts course', 400);
