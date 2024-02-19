#!/usr/bin/node
/* A script that imports a dictionary of occurrences by user id and computes a dictionary of user ids by occurrence.*/
const dict = require('./101-data').dict;

const convertedArr = Object.entries(dict);

const occurrenceDict = {};

convertedArr.forEach(element => {
	occurrenceDict[element[1]] ? occurrenceDict[element[1]].
		push(element[0]) : occurrenceDict[element[1]] =  [element[0]];
}
);

console.log(occurrenceDict);
