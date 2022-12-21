#!/usr/bin/node
const fs = require('fs');

const file1 = process.argv[2];
const file2 = process.argv[3];
const output = process.argv[4];

// Read the contents of the first file
const file1Content = fs.readFileSync(file1, 'utf8');

// Read the contents of the second file
const file2Content = fs.readFileSync(file2, 'utf8');

// Concatenate the contents of the two files
const outputContent = file1Content + file2Content;

// Write the concatenated contents to the output file
fs.writeFileSync(output, outputContent);
