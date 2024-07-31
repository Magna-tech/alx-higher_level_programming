#!/usr/bin/node

const request = require('request');
const fs = require('fs');

// Check if the URL and file path arguments are provided
if (process.argv.length !== 4) {
  console.error('Usage: ./fetchAndSave.js <url> <file_path>');
  process.exit(1);
}

// Get the URL and file path from command-line arguments
const url = process.argv[2];
const filePath = process.argv[3];

// Fetch the webpage content
request(url, (error, response, body) => {
  if (error) {
    console.error('Error fetching the URL:', error);
    process.exit(1);
  }

  // Check if the request was successful
  if (response.statusCode !== 200) {
    console.error(`Failed to fetch the URL. Status code: ${response.statusCode}`);
    process.exit(1);
  }

  // Write the response body to the specified file
  fs.writeFile(filePath, body, 'utf8', (err) => {
    if (err) {
      console.error('Error writing to file:', err);
    } else {
      console.log(`Successfully saved webpage content to ${filePath}`);
    }
  });
});
