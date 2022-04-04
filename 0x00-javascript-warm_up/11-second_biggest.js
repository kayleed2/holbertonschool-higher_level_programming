#!/usr/bin/node
// Prints a message depending on passed arguments

if (process.argv.length < 4) {
  console.log(0);
} else {
  const args = process.argv.slice(2).sort();
  console.log(args[args.length - 2]);
}
