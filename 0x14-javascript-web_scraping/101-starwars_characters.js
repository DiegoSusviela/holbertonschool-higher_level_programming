#!/usr/bin/node
const request = require('request');

request('https://swapi-api.hbtn.io/api/films/' + process.argv[2], function (error, response, body) {
  if (error)
    console.error(error);
  const path = JSON.parse(body).characters;
  console.log(path);
  let arr = Object.keys(path).map(key => path[key]);
  console.log(arr);

  for(i = 0; i < arr.length; i++) {
    request(arr[i], function (error, response, body) {
      if (error)
        console.error(error);
      const name = JSON.parse(body).name;
      console.log(name);
    });
  };
});
