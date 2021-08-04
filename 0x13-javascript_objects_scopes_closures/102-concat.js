#!/usr/bin/node
let fs = require('fs');
let TA = fs.readFileSync(process.argv[2], 'utf8');
let TB = fs.readFileSync(process.argv[3], 'utf8');
fs.writeFileSync(process.argv[4], TA + TB);
