#!/usr/bin/node

$(function () {
    $.getJSON('https://fourtonfish.com/hellosalut/?lang=fr', function (data) {
      $('DIV#hello').html(data.hello);
});
})
