#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (err, response, body) {
  if (err) throw err;
  if (response.statusCode === 200) {
    let com = {};
    let tas = JSON.parse(body);
    for (let i in tas) {
      let task = tas[i];
      if (task.com === true) {
        if (com[task.userId] === undefined)
          com[task.userId] = 1;
        else
          com[task.userId]++;
      }
    }
    console.log(com);
  } else
    console.log('An error occured. Status code: ' + response.statusCode);
});
