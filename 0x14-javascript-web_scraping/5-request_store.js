#!/usr/bin/node
const request = require('request');
let text;
request(process.argv[2], function (error, response, body) {
  if (err) throw err;
  text = body;
  require('fs').writeFile(process.argv[3], text, 'utf-8', (err) => {
  if (err) throw err;
  });
});
