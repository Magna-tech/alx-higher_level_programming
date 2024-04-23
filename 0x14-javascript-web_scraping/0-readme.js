#!/usr/bin/node

const fs = require('fs');

// Check if file path is provided
if (process.argv.length < 3) {
  console.error('Usage: node read_file.js <file_path>');
  process.exit(1);
}

// Get file path from command line argument
const filePath = process.argv[2];

// Read file asynchronously
fs.readFile(filePath, 'utf-8', (err, data) => {
  if (err) {
    console.error(err);
  } else {
    console.log(data);
  }
});
