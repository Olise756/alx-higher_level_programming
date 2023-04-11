#!/usr/bin/node
const size = Math.floor(Number(process.argv[2]));
if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let g = 0; g < size; g++) {
    let row = '';
    for (let i = 0; i < size; i++) row += 'X';
    console.log(row);
  }
}
