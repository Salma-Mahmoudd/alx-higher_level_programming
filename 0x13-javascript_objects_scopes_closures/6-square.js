#!/usr/bin/node
const Squar = require('./5-square');
module.exports =
class Square extends Squar {
  charPrint (c) {
    let sqChar = 'X';
    if (c !== undefined) sqChar = c;
    for (let i = 0; i < this.height; i++) {
      console.log(sqChar.repeat(this.width));
    }
  }
};
