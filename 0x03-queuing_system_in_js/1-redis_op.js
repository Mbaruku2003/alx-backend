import { createClient, print } from 'redis';

const client = createClient({ host: '127.0.0.1', port: 6379 });
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});
function displaySchoolValue(schoolName) {
  client.get(schoolName, (err, result) => {
    if (err) {
      console.log(`Error retrieving key "${schoolName}": ${err.message}`);
    } else {
      console.log(result);
    }
  });
}
function setNewSchool(schoolName, value, callback) {
  client.set(schoolName, value, (err, res) => {
    print(err, res);
    if (callback) callback();
  });
}


displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100', () => {
  displaySchoolValue('HolbertonSanFrancisco');
});
