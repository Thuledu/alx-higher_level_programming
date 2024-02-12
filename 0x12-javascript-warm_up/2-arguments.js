#!/usr/bin/node
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
