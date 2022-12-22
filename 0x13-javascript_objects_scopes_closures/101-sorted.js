#!/usr/bin/node
const dict = require('./101-data.js').dict;

const userIds = {};

for (const [userId, i] of Object.entries(dict)) {
  if (userIds[i]) {
    userIds[i].push(userId);
  } else {
    userIds[i] = [userId];
  }
}

console.log(userIds);
