#!/usr/bin/node
/* A script that imports an array and computes a new array. */
const list = require('./100-data').list;

console.log('Initial list:', list);

const newList = list.map((value, index) => value * index);

console.log('New list:', newList);
