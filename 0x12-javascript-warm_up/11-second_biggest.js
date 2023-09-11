#!/usr/bin/node
const arr = process.argv.slice(2);
if (arr.length <= 1) {
  console.log(0);
} else {
  arr.sort((a, b) => a - b);
  console.log(arr[arr.length - 2]);
}
