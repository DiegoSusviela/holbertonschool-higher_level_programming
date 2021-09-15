#!/usr/bin/node
const request = require('request');
let dic = {};
let cont = 0;
let pos1 = 0;
let pos2 = 0;
request(process.argv[2], function (
  error, response, body) {
  if (err) throw err;
  dic = JSON.parse(body);
  for (pos1 = 0; pos1 < dic.results.length; pos1++) {
    for (pos2 = 0; pos2 < dic.results[pos1].characters.length; pos2++) {
      if (dic.results[pos1].characters[pos2].includes('/18/'))
        cont++;
    }
    console.log(cont);
  }
});
