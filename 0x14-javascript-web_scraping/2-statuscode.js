#!/usr/bin/node

const request = require('request');
request(process.argv[2], function (err, response) {
  if (err) throw err;
  console.log('code: ' + response.statusCode);
});
