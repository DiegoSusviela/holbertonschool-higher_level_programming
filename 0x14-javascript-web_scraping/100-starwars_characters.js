#!/usr/bin/node
const request = require('request');
const options = { json: true };
request('https://swapi-api.hbtn.io/api/films/' + process.argv[2], options, (error, res, body) => {
  if (error)
    return console.log(error);
  if (!error && res.statusCode === 200) {
    body.characters.forEach(element => {
      request(element, options, (error, res, body) => {
        if (error)
          return console.log(error);
        if (!error && res.statusCode === 200)
          console.log(body.name);
      });
    });
  }
});
