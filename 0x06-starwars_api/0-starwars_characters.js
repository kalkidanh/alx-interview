#!/usr/bin/node
// script that prints the characters of Star Wars using the SWAPI.
const request = require('request');

if (process.argv.length === 3) {
  const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}/`;

  // Make an API request.
  request(url, async (error, response, body) => {
    if (error) {
      console.log(error);
    } else {
      // Star Wars characters url.
      const urlList = JSON.parse(body).characters;

      // Get The Star Wars characters.
      for (const chars of urlList) {
        const charList = () => {
          return new Promise((resolve, reject) => {
            request(chars, async (error, response, body) => {
              if (error) {
                console.log(error);
              }
              resolve(JSON.parse(body).name);
            });
          });
        };
        console.log(await charList());
      }
    }
  });
}
