#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let ocurr = 0;
  for (let pos in list) {
    if (list[pos] === searchElement) {
      ocurr++;
    }
  }
  return ocurr;
};
