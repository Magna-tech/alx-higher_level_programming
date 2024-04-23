#!/usr/bin/node

const fs = require('fs');

// Check if the file path and string to write arguments are provided
if (process.argv.length < 4) {
  console.error('Usage: node write_file.js <file_path> <string_to_write>');
  process.exit(1);
}

// Get file path and string to write from command line arguments
const filePath = process.argv[2];
const stringToWrite = process.argv[3];

// Write the given string to file
fs.writeFile(filePath, stringToWrite, 'utf-8', (err) => {
  if (err) {
    console.error(err);
  } else {
    console.log(`Successfully wrote "${stringToWrite}" to ${filePath}`);
  }
});
