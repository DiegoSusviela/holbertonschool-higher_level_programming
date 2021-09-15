#!/usr/bin/node
const request = require('request');
let lis = [];
let pos1 = 0;
const dic = {};
let clave = '';

request(process.argv[2], function (error, response, body) {
  if (err) throw err;
  lis = JSON.parse(body);
  for (pos1 = 0; pos1 < lis.length; pos1++) {
    clave = lis[pos1].userId;
    if (lis[pos1].completed === true) {
    if (!dic[clave]) 
      dic[clave] = 1;
    else
      dic[clave] += 1;
    }
    console.log(dic);
  }
});
