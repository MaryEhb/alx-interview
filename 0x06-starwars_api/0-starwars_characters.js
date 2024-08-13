#!/usr/bin/node
// 0. Star Wars Characters

const request = require('request');
const util = require('util');
const args = process.argv;

const requestGet = util.promisify(request.get);

(async () => {
  if (args.length < 3) return;
  const movieUrl = 'https://swapi-api.alx-tools.com/api/films/' + args[2];
  try {
    const movieResponse = await requestGet(movieUrl);
    const movie = JSON.parse(movieResponse.body);

    if (movie.characters === undefined) return;

    for (const characterUrl of movie.characters) {
      try {
        const characterResponse = await requestGet(characterUrl);
        const character = JSON.parse(characterResponse.body);
        console.log(character.name);
      } catch (characterError) {
        console.error('Error fetching character data:', characterError);
      }
    }
  } catch (movieError) {
    console.error('Error fetching movie data:', movieError);
  }
})();
