#!/usr/bin/node
// Prints a message depending on passed arguments

const x = parseInt(process.argv[2]);

if (isNaN(x)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < x; i++) {
    const string = 'X'.repeat(x);
    console.log(string);
  }
}
