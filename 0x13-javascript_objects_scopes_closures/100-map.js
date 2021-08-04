#!/usr/bin/node
let list = require('./100-data.js').list;
console.log(list);
let mapa = list.map((x, index) => x * index);
console.log(mapa);
