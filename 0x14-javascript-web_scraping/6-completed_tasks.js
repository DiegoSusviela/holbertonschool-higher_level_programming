#!/usr/bin/node
const request = require('request');
const resdic = { json: true };
const results = {};
request(process.argv[2], resdic, (error, res, body) => {
  if (error) {
    return console.log(error);
  }
  if (!error && res.statusCode === 200) {
    body.forEach(tasks => {
      if (tasks.completed) {
        if (!results[tasks.userId]) {
          results[tasks.userId] = 1;
        } else {
          results[tasks.userId] += 1;
        }
      }
    });
    console.log(results);
  }
});
