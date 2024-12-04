import { expect } from 'chai';
import kue from 'kue';
import createPushNotificationsJobs from './8-job.js';

describe('createPushNotificationsJobs', () => {
    let queue;

    // Setup before tests
    before(() => {
        queue = kue.createQueue();
        kue.testMode.enter(); // Enter test mode
    });

    // Cleanup after tests
    afterEach(() => {
        kue.testMode.clear(); // Clear the queue after each test
    });

    after(() => {
        kue.testMode.exit(); // Exit test mode after all tests
    });

    it('should display an error message if jobs is not an array', () => {
        const invalidInput = 'not an array';

        expect(() => createPushNotificationsJobs(invalidInput, queue)).to.throw(
            'Jobs is not an array'
        );
    });

    it('should create two new jobs to the queue', () => {
        const jobs = [
            { phoneNumber: '4153518780', message: 'This is the code 1234 to verify your account' },
            { phoneNumber: '4153518781', message: 'This is the code 5678 to verify your account' },
        ];

        createPushNotificationsJobs(jobs, queue);

        // Validate job count in the queue
        expect(queue.testMode.jobs.length).to.equal(2);

        // Validate job details
        expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
        expect(queue.testMode.jobs[0].data).to.deep.equal(jobs[0]);

        expect(queue.testMode.jobs[1].type).to.equal('push_notification_code_3');
        expect(queue.testMode.jobs[1].data).to.deep.equal(jobs[1]);
    });

    it('should call event listeners for job lifecycle', (done) => {
        const jobData = { phoneNumber: '4153518782', message: 'This is a test notification' };
        const job = queue.create('push_notification_code_3', jobData);

        let completeCalled = false;
        let failedCalled = false;
        let progressCalled = false;

        // Mock event listeners
        job.on('complete', () => {
            completeCalled = true;
        });
        job.on('failed', () => {
            failedCalled = true;
        });
        job.on('progress', () => {
            progressCalled = true;
        });

        job.save(() => {
            // Simulate events
            job.emit('progress', 50);
            job.emit('complete');

            // Validate events were called
            expect(progressCalled).to.be.true;
            expect(completeCalled).to.be.true;
            expect(failedCalled).to.be.false;

            done();
        });
    });
});

