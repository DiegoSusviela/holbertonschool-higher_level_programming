#!/usr/bin/node
const req = require('request');

req.get(process.argv[2], function (err, response) {
  if (err) throw err;
  require('fs').appendFile(process.argv[3], response.body, function (err) {
    if (err) throw err;
  });
});
