#!/opt/homebrew/bin/node
// #!/usr/bin/node
// Prints a message depending on passed arguments

const argOne = process.argv[2];
const argTwo = process.argv[3];
const string = argOne + ' is ' + argTwo;
console.log(string);
