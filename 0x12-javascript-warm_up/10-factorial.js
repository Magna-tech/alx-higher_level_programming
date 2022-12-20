#!/usr/bin/node
function factorial(a) {
  if (a === 1) {
    return 1
  }
  return a * factorial(a - 1);
}
if (process.argv.length < 3) {
  console.log(1);
} else {
  console.log(factorial(~~process.argv[2]));
}
