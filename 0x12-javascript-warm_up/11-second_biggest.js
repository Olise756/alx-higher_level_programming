#!/usr/bin/node

if (process.argv.length < 4) {
  console.log('0');
} else {
  const size = process.argv.length;
  const ints = [];
  for (let c = 2; c < size; c++) {
    ints[c - 2] = parseInt(process.argv[c]);
  }
  ints.sort(function (a, b) { return b - a; });
  console.log(ints[1]);
}
