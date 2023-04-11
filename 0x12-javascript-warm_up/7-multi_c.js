#!/usr/bin/node
const y = Math.floor(Number(process.argv[2]));
if (isNaN(y)) {
  console.log('Missing number of occurrences');
} else {
  for (let c = 0; c < y; c++) {
    console.log('C is fun');
  }
}
