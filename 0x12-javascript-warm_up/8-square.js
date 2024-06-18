#!/usr/bin/node

const args = process.argv.slice(2);
const num = parseInt(args[0], 10);

if (isNaN(num)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < args[0]; i++) {
    let square = '';
    for (let j = 0; j < args[0]; j++) {
      square += 'X';
    }
    console.log(square);
  }
}
