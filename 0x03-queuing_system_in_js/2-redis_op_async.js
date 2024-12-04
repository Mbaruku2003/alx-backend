import { createClient, print } from 'redis';
import { promisify } from 'util';

const client = createClient({ host: '127.0.0.1', port: 6379 });
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});
const getAsync = promisify(client.get).bind(client);
async function displaySchoolValue(schoolName) {
  try {
    const result = await getAsync(schoolName);
    console.log(result);
  } catch (err) {
    console.log(`Error retreiving key "${schoolName}": ${err.message}`);
  }
}
function setNewSchool(schoolName, value, callback) {
  client.set(schoolName, value, (err, res) => {
    print(err, res);
    if (callback) callback();
  });
}
(async () => {
  await displaySchoolValue('Holberton');
  setNewSchool('HolbertonSanFrancisco', '100', async () => {
    await displaySchoolValue('HolbertonSanFrancisco');
  });
})();
