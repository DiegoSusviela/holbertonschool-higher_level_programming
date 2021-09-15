#!/usr/bin/node
const request = require('request');
let resdic = {};
let count = 0;
let pos1 = 0;
let pos2 = 0;
request(process.argv[2], function (
  error, response, body) {
  if (err) throw err;
  resdic = JSON.parse(body);
    for (pos1 = 0; pos1 < resdic.results.length; pos1++) {
      for (pos2 = 0; pos2 < resdic.results[pos1].characters.length; pos2++) {
        if (resdic.results[pos1].characters[pos2].includes('/18/')) {
          count++;
        }
      }
    }
    console.log(count);
});
