#!/usr/bin/node
exports.converter = function (base) {
  function conv (n) {
    return n.toString(base);
  }
  return conv;
};
