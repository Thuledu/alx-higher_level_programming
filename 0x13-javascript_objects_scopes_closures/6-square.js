#!/usr/bin/node
/* A class Square that defines a square and inherits from Square of 5-square.js */
module.exports = class Square extends require('./5-square.js') {
	constructor(size) 
	{
		super(size, size);
	}
charPrint(c) {
	if (c === undefined) 
	{
		c = 'X';
	}
	for (let i = 0; i < this.height; i++)
	{
		let row = '';
		for (let j = 0; j < this.width; j++)
		{
			row += c;
		}
		console.log(row);
	}
}
}
