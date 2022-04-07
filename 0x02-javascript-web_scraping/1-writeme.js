#!/usr/bin/node
// A script that reads and prints the content of a file

const filePath = process.argv[2];
const string = process.argv[3];
const fs = require('fs');

fs.writeFile(filePath, string, err => {
  if (err) {
    console.error(err);
  }
});
