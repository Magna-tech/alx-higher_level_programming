#!/usr/bin/node

const request = require('request');

// Check if the API URL argument is provided
if (process.argv.length < 2) {
  console.error('Usage: ./filename <api_url>');
  process.exit(1);
}

// Get API URL from command line argument
const apiUrl = process.argv[2];

// Make a GET request to the Star Wars API films endpoint
request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else {
    if (response.statusCode === 200) {
      const filmData = JSON.parse(body).results;
      let wedgeMoviesCount = 0;

      // Iterate through films data to check if Wedge Antilles is present
      filmData.forEach(film => {
        const characters = film.characters;
        if (characters.includes('https://swapi-api.alx-tools.com/api/people/18/')) {
          wedgeMoviesCount++;
        }
      });

      console.log(`${wedgeMoviesCount}`);
    } else {
      console.error(`Error: Unable to fetch films data. Status code: ${response.statusCode}`);
    }
  }
});
