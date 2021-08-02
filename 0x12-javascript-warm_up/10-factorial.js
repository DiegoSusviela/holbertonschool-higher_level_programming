#!/usr/bin/node
function factorial (x) {
  const number = parseInt(x);
  if (isNaN(number) || x === 1) {
    return 1;
  }
  return (x * factorial(number - 1));
}
console.log(factorial(process.argv[2]));
