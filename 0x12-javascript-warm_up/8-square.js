#!/usr/bin/node
/* A script that prints a square  */
const argument = process.argv[2];
const size = parseInt(argument);

if (isNaN(size) || size <= 0) 
{
	console.log('Missing size');
} 
else 
{
	for (let i = 0; i < size; i++) 
	{
		console.log('X'.repeat(size));
	}
}
