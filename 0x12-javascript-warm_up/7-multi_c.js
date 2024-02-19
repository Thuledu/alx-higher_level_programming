#!/usr/bin/node
/* A script that prints x times “C is fun”  */
const argument = process.argv[2];
const numOccurrences = parseInt(argument);

if (isNaN(numOccurrences) || numOccurrences <= 0) 
{
	console.log('Missing number of occurrences');
} 
else 
{
	for (let i = 0; i < numOccurrences; i++)
	{
		console.log('C is fun');
	}
}
