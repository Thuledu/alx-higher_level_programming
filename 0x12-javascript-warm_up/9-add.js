#!/usr/bin/node
/**
 * Prints the addition of two integers
 * @a - The first integer
 * @b - The second integer
 */
function add(a, b) 
{
	console.log(a + b);
}

const arg1 = parseInt(process.argv[2]);
const arg2 = parseInt(process.argv[3]);

if (isNaN(arg1) || isNaN(arg2)) 
{
	console.log('Missing size');
} 
else 
{
	add(arg1, arg2);
}
