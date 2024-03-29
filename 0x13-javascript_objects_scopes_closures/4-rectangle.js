#!/usr/bin/node
/* A class Rectangle that defines a rectangle.*/
module.exports = class Rectangle {
	constructor(w, h) 
	{
		if (w > 0 && h > 0) 
		{
			this.width = w;
			this.height = h;
		} 
		else 
		{
			Object.create(null);
		}
	}
print() {
	if (this.width === 0 || this.height === 0) 
	{
		console.log('');
	}
	else
	{
		for (let i = 0; i < this.height; i++)
		{
			let row = '';
			for (let j = 0; j < this.width; j++)
			{
				row += 'X';
			}
			console.log(row);
		}
	}
}

rotate() {
	let temp = this.width;
	this.width = this.height;
	this.height = temp;
}

double() {
	this.width *= 2;
	this.height *= 2;
}
}

