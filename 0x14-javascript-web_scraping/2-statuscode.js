#!/usr/bin/node

const request = require('request');

// Check if URL argument is provided by user
if (process.argv.length < 3) {
  console.error('Usage: node get_status_code.js <URL>');
  process.exit(1);
}

// Get URL from command line arguments
const url = process.argv[2];

// Make a GET request
request.get(url, (error, response) => {
  if (error) {
    console.error('Error:', error);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
