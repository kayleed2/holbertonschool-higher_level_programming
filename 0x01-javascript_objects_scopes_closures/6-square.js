#!/usr/bin/node
// Defines empty class Rectangle

const square = require('./5-square');

class Square extends square {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c !== undefined) {
      for (let i = 0; i < this.height; i++) {
        const string = 'C'.repeat(this.width);
        console.log(string);
      }
    } else {
      for (let i = 0; i < this.height; i++) {
        const string = 'X'.repeat(this.width);
        console.log(string);
      }
    }
  }
}
module.exports = Square;
