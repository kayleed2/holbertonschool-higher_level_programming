#!/usr/bin/node
// Prints a message depending on passed arguments

if (process.argv[2]) {
  console.log(process.argv[2]);
} else {
  console.log('No argument');
}
