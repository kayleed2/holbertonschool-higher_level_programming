#!/usr/bin/node
// Prints a message depending on passed arguments

function add (a, b) {
  const result = a + b;
  return result;
}

const a = parseInt(process.argv[2]);
const b = parseInt(process.argv[3]);

if (isNaN(a) || isNaN(b)) {
  console.log('NaN');
} else {
  console.log(add(a, b));
}
