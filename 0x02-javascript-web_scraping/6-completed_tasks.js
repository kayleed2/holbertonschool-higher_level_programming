#!/usr/bin/node
// A script that display the status code of a GET request.

const request = require('request');
const url = process.argv[2];
const newDict = {};

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const jsonContent = (JSON.parse(body));
    for (let i = 0; i < jsonContent.length; i++) {
      if (jsonContent[i].completed === true) {
        if (jsonContent[i].userId in newDict) {
          newDict[jsonContent[i].userId] += 1;
        } else {
          newDict[jsonContent[i].userId] = 1;
        }
      }
    }
  }
  console.log(newDict);
});
