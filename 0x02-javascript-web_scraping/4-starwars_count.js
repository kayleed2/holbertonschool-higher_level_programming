#!/opt/homebrew/bin/node
// #!/usr/bin/node
// A script that display the status code of a GET request.

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/';

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const jsonContent = (JSON.parse(body));
    let i = 0;
    for (i in jsonContent.results) {
      console.log(i);
    }
  }
});
