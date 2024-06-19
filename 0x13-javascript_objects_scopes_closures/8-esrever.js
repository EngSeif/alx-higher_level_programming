#!/usr/bin/node
exports.esrever = function (list) {
  const Reversed = [];
  for (let i = list.length - 1; i >= 0; i--) {
    Reversed.push(list[i]);
  }
  return Reversed;
};
