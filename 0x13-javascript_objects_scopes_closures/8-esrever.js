#!/usr/bin/node
exports.esrever = function (list) {
  const rev = [];
  while (list.length !== 0) { rev.push(list.pop()); }
  return rev;
};
