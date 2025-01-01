#!/usr/bin/node
const request = require('request');

const argv = process.argv;
const urlFilm = 'https://swapi-api.hbtn.io/api/films/';
const urlMovie = `${urlFilm}${argv[2]}/`;

request(urlMovie, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const movieData = JSON.parse(body);
    const characters = movieData.characters;

    if (characters && characters.length > 0) {
      const limit = characters.length;
      CharRequest(0, characters, limit);
    }
  } else {
    console.error(error);
  }
});

function CharRequest (idx, characters, limit) {
  if (idx === limit) {
    return;
  }

  request(characters[idx], function (error, response, body) {
    if (!error && response.statusCode === 200) {
      const characterData = JSON.parse(body);
      console.log(characterData.name);
      idx++;
      CharRequest(idx, characters, limit);
    } else {
      console.error('Error:', error);
    }
  });
}
