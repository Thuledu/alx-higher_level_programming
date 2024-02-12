#!/usr/bin/node
/**
 * Computes and prints the factorial of an integer
 * @num - The integer to compute the factorial of
 * @returns - The factorial of the given integer
 */
function factorial(num) {
	if (num < 0) 
	{
		return (-1);
	}

	if (num === 0 || num === 1) 
	{
		return 1;
	}

	return (num * factorial(num - 1));
}
console.log(factorial(Number(process.argv[2])));
