#!/usr/bin/node
/* script that prints the first argument passed to it */
const argument = process.argv[2];

if (!argument) 
{
	console.log('No argument');
} 
else 
{
	console.log(argument);
}
