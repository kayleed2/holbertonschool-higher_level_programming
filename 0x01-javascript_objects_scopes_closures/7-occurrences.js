#!/usr/bin/node
// a function that returns the number of occurrences in a list

exports.nbOccurences = function (list, searchElement) {
  let occur = 0;
  for (const el of list) {
    if (el === searchElement) {
      occur += 1;
    }
  }
  return occur;
};
