#!/usr/bin/node
const request = require('request-promise');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

async function fetchData (url) {
  try {
    const filmResponse = await request({
      url,
      json: true
    });
    const charUrl = filmResponse.characters;
    for (let i = 0; i < charUrl.length; i++) {
      const characterResponse = await request({
        uri: charUrl[i],
        json: true
      });
      console.log(characterResponse.name);
    }
  } catch (error) {
    console.error('Error fetching data:', error);
  }
}

fetchData(url);
