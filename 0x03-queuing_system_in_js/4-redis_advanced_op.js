import { createClient, print } from 'redis';

const client = createClient({ host: '127.0.0.1', port: 6379 });
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});
const hashKey = 'HolbertonSchools';
const locations = {
  Portland: 50,
  Seattle: 80,
  'New York': 20,
  Bogota: 20,
  Cali: 40,
  Paris: 2,
};
for (const [field, value] of Object.entries(locations)) {
  client.hset(hashKey, field, value, print);
}
client.hgetall(hashKey, (err, result) => {
  if (err) {
    console.log(`Error retreiving hash: ${err.message}`);
  } else {
    console.log(result);
  }
});
