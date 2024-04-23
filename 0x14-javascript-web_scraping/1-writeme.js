#!/usr/bin/node

const fs = require('fs');

// Check if the file path and string to write arguments are provided
if (process.argv.length < 4) {
  console.error('Usage: ./1-writeme.js <file_path> <string_to_write>');
  process.exit(1);
}

// Get the file path and string to write from command line arguments
const fileP = process.argv[2];
const string = process.argv[3];

// Write the given string to file
fs.writeFile(fileP, string, 'utf-8', (err) => {
  if (err) {
    console.error(err);
  } else {
    console.log(`Successfully wrote "${string}" to ${fileP}`);
  }
});
