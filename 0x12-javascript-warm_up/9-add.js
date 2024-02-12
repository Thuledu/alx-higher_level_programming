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

add(Number(process.argv[2]), Number(process.argv[3]));
