#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;
const options = {
  url,
  json: true
};

request(options, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const title = body.title;
    console.log(title);
  }
});
