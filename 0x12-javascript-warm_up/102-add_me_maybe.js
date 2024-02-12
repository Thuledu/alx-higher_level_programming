#!/usr/bin/node
/**
 * Increments a number and calls a function
 * @number - The number to increment
 * @theFunction - The function to call
 */
exports.addMeMaybe = function incrementAndCall(number, theFunction) 
{
	theFunction(++number);
}
