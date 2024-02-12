#!/usr/bin/node
/**
 * Computes and prints the factorial of an integer
 * @num - The integer to compute the factorial of
 * @returns - The factorial of the given integer
 */
function computeFactorial(num) {
	if (isNaN(num)) 
	{
		console.log(1);
		return 1;
	}

	if (num === 0 || num === 1) 
	{
		console.log(1);
		return 1;
	}

	const factorial = num * computeFactorial(num - 1);
	console.log(factorial);
	return factorial;
}
const argument = parseInt(process.argv[2]);
computeFactorial(argument);
