#!/usr/bin/node

const args = process.argv.slice(2);

if (args[1] === undefined) {
  console.log(0);
} else {
  args.sort((a, b) => b - a);
  console.log([args[1]]);
}
