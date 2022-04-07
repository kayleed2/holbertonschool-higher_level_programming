#!/usr/bin/node
// A script that display the status code of a GET request.

const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const location = process.argv[3];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(location, body, err => {
      if (err) {
        console.error(err);
      }
    });
  }
});
