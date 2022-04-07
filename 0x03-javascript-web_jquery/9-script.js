#!/usr/bin/node

$(function () {
    $.getJSON('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
      $('#list_movies');
    });
});
