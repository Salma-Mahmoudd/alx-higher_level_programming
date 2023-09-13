#!/usr/bin/node
const dict = require('./101-data.js').dict;
const arr = {};
for (const [value, key] of Object.entries(dict)) {
  if (key in arr) {
    arr[key].push(value);
  } else { arr[key] = [value]; }
}
console.log(arr);
