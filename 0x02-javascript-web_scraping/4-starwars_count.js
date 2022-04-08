#!/opt/homebrew/bin/node
// #!/usr/bin/node
// A script that display the status code of a GET request.

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/';

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const jsonContent = JSON.parse(body).results;
    let i = 0;
    for (const el in jsonContent) {
      const chars = jsonContent[el].characters;
      for (const x in chars) {
        if (chars[x].includes('/18/')) {
          i += 1;
        }
      }
    }
    console.log(i);
  }
});
