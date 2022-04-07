#!/opt/homebrew/bin/node
// #!/usr/bin/node

// const request = require('request');

// const response = request('https://swapi-api.hbtn.io/api/people/5/?format=json', function (error, response, body) {
//     if (error) {
//       console.log(error);
//     } else {
//       const name = JSON.parse(body).name;
//     }
//   });

$(function () {
  $.getJSON('https://swapi-api.hbtn.io/api/people/5/?format=json', function (data) {
    $('#character').html(data.name);
  });
});
