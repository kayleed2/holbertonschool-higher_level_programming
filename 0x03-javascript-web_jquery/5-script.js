#!/usr/bin/node
$(function () {
    $('#add_item').on('click', function() { 
        $('ul.my_list').append('<li>Item</li>');
    });
})
