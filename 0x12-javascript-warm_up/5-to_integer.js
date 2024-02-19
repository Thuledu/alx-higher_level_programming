#!/usr/bin/node
/* A script that prints My number: <first argument converted in integer> if the first argument can be converted to an integer.  */
const argument = process.argv[2];
const parsedInt = parseInt(argument);

if (!isNaN(parsedInt)) 
{
	console.log(`My number: ${parsedInt}`);
} 
else 
{
	console.log('Not a number');
}
