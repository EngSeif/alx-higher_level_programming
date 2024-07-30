#!/usr/bin/node
const request = require('request');

const url = process.argv[2];
let count = 0;
const options = {
  url,
  json: true
};

request(options, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    for (let i = 0; i < body.results.length; i++) {
      const Persons = body.results[i].characters;
      for (let j = 0; j < Persons.length; j++) {
        if (Persons[j].includes('18')) {
          count = count + 1;
        }
      }
    }
    console.log(count);
  }
});
