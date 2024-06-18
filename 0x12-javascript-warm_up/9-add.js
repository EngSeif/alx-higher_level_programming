#!/usr/bin/node

const args = process.argv.slice(2);
const num1 = parseInt(args[0], 10);
const num2 = parseInt(args[1], 10);

function add (a, b) {
  return (a + b);
}

console.log(add(num1, num2));
