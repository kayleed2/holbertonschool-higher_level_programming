#!/usr/bin/node
// A script that display the status code of a GET request.

const request = require('request');
const movieId = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + movieId;

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
