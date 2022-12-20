#!/usr/bin/node
if (isNaN(process.argv[2])) {
  console.log('Missing size');
}
const size = ~~process.argv[2];
let i = 0;
let line = 'X';
for (i = 0; i < size - 1; i++) {
  line += 'X';
}
i = 0;
while (i < size) {
  console.log(line);
  i++;
}
