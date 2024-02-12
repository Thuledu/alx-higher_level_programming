#!/usr/bin/node
/**
 * Executes a function x times
 * @x - The number of times to execute the function
 * @theFunction - The function to execute
 */
function callMeMoby(x, theFunction) {
	for (let i = 0; i < x; i++) 
	{
		theFunction();
	}
}

module.exports = { callMeMoby };
