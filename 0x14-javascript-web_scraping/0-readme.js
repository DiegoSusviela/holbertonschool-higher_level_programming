#!/usr/bin/node

require('fs').readFile(process.argv[2], 'utf-8', function (err, data) {
  if (err) throw err;
  console.log(data);
})
;
