import { createQueue } from "kue";

const blacklisted = ['4153518780', '4153518781'];
function sendNotification(phoneNumber, message, job, done) {
  const progress = 100

  job.progress(0, progress);

  if (blacklisted.includes(phoneNumber)) {
    done(Error(`Phone number ${phoneNumber} is blacklisted`));
    return;
  }

  job.progress(50, progress);

  console.log(
    `Sending notification to ${phoneNumber}, with message: ${message}`
  );

  done();
}

const queue = createQueue();

queue.process("push_notification_code_2", 2, (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message, job, done);
});
