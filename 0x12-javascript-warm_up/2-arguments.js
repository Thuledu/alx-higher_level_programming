#!/usr/bin/node
/* script that prints a message depending of the number of arguments passed */
const argsCount = process.argv.length - 2;

switch (argsCount) {
	case 0:
		console.log('No argument');
		break;
	case 1:
		console.log('Argument found');
		break;
	default:
		console.log('Arguments found');
		break;
}
