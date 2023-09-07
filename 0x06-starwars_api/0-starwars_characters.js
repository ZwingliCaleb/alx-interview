#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];

if (!movieId) {
  console.error('Please provide a movie ID as a command-line argument.');
  process.exit(1);
}

const swapiUrl = `https://swapi.dev/api/films/${movieId}/`;

request(swapiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    process.exit(1);
  }

  if (response.statusCode !== 200) {
    console.error('Error:', response.statusCode, response.statusMessage);
    process.exit(1);
  }

  const filmData = JSON.parse(body);

  if (!filmData.characters || filmData.characters.length === 0) {
    console.log('No characters found for this movie.');
  } else {
    fetchCharacterNames(filmData.characters);
  }
});

function fetchCharacterNames(characterUrls) {
  const characterPromises = characterUrls.map(url =>
    new Promise((resolve, reject) => {
      request(url, (error, response, body) => {
        if (error) {
          reject(error);
        }

        const characterData = JSON.parse(body);
        resolve(characterData.name);
      });
    })
  );

  Promise.all(characterPromises)
    .then(names => {
      names.forEach(name => console.log(name));
    })
    .catch(error => {
      console.error('Error:', error);
      process.exit(1);
    });
}

