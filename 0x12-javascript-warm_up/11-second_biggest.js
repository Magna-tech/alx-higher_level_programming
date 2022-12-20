#!/usr/bin/node
if (process.argv.length < 4) {
  console.log(0);
} else {
  const args = process.argv.slice(2);
  const sorted = args.sort((a, b) => a - b);
  console.log(sorted.slice(-2, -1)[0]);
}
