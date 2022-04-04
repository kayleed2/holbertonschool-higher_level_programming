#!/usr/bin/node
// Prints a message depending on passed arguments

function factorial (x) {
  if (x < 0 || isNaN(x)) {
    return 1;
  } else if (x === 0) {
    return 1;
  } else {
    return (x * factorial(x - 1));
  }
}
console.log(factorial(process.argv[2]));
