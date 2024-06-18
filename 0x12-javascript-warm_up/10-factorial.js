#!/usr/bin/node

const args = process.argv.slice(2);
const num1 = parseInt(args[0], 10);

function factorial (a) {
  if (a === 1) {
    return a;
  }
  return (a * factorial(a - 1));
}

if (isNaN(num1)) {
  console.log(1);
} else {
  console.log(factorial(num1));
}
