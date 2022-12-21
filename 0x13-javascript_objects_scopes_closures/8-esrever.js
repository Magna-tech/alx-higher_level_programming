#!/usr/bin/node
exports.esrever = function (list) {
  const newlist = [];
  let i = list.length - 1;
  let j = 0;
  for (j = 0; j < list.length; j++) {
    newlist[j] = list[i];
    i = i - 1;
  }
  return newlist;
};
