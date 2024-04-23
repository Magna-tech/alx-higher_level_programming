#!/usr/bin/node
const request = require('request');

// Check if the movie ID argument is provided
if (process.argv.length < 3) {
  console.error('Usage: ./3-starwars_title.js <movie_id>');
  process.exit(1);
}

// Get the movie ID from command line argument
const movieId = process.argv[2];

// Construct a URL with the provided movie ID
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Make a GET request to the Star Wars API
request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else {
    if (response.statusCode === 200) {
      const movieData = JSON.parse(body);
      console.log(`${movieData.title}`);
    } else {
      console.error(`Error: Unable to fetch movie with ID ${movieId}. Status code: ${response.statusCode}`);
    }
  }
});
