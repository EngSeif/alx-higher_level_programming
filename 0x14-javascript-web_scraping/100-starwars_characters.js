#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;
const options = {
  url,
  json: true
};

const op = {
  url: '',
  json: true
};

request(options, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    for (let i = 0; i < body.characters.length; i++) {
      op.url = body.characters[i];
      request(op, (err, r, b) => {
        if (err) {
          console.log(err);
        } else {
          console.log(b.name);
        }
      });
    }
  }
});
