#!/usr/bin/node
const request = require('request');
const data = {};
let id;
const url = process.argv[2];
const options = {
  url,
  json: true
};

request(options, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    for (let i = 0; i < body.length; i++) {
      if (body[i].completed) {
        id = body[i].userId;
        if (id in data) {
          data[id] += 1;
        } else {
          data[id] = 1;
        }
      }
    }
  }
  console.log(data);
});
