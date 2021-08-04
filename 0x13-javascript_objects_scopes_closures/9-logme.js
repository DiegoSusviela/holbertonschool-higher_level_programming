#!/usr/bin/node
let conter = 0;
exports.logMe = function (item) {
  console.log(conter + ': ' + item);
  conter++;
};
