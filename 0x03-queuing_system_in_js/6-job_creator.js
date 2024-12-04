import kue from 'kue';

const queue = kue.createQueue({ host: '127.0.0.1', port: 6379 });
const jobData = {
  phoneNumber: '1234567890',
  message: 'This is the message content',
};
const job = queue.create('push_notification_code', jobData)
  .save((err) => {
    if (!err) {
      console.log(`Notification job created: ${job.id}`);
    } else {
      console.error(`Error creating job: ${err.message}`);
    }
  });
job.on('complete', () => {
  console.log('Notification job completed');
});
job.on('failed', () => {
  console.log('Notification job failed');
});
