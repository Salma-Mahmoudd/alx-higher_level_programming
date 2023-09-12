#!/usr/bin/node
const Sq = require('./5-square');
module.exports =
class Square extends Sq {
  charPrint (c) {
    let sqChar = 'X';
    if (c !== undefined) sqChar = c;
    for (let i = 0; i < this.height; i++) {
      console.log(sqChar.repeat(this.width));
    }
  }
};
