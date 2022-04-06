#!/usr/bin/node
// a function that returns reversed version of a list

exports.esrever = function (list) {
  const newArr = [];
  const length = list.length - 1;
  for (let i = length; i >= 0; i--) {
    newArr.push(list[i]);
  }
  return newArr;
};
