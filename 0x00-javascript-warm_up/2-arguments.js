#!/usr/bin/node
// Prints a message depending on passed arguments

const number = process.argv.length;

if (number <= 2) {
  console.log('No argument');
} else {
  console.log('Arguments found');
}
