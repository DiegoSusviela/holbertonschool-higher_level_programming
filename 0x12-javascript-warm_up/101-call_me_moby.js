#!/usr/bin/node
exports.callMeMoby = function (x, theFunction) {
	for (let iter = 0; iter < x; iter++) {
		theFunction();
	}
};
