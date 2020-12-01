console.log("2020 - 01 - Part 1");
var fs = require('fs');
// Read input
var input = fs.readFileSync(__dirname + '/input.txt', 'utf8').toString().split('\n');
function twoSum(inputs, target) {
    var indexByNumber = {};
    for (var i = 0; i < inputs.length; i++) {
        var number = inputs[i];
        var difference = target - number;
        if (typeof indexByNumber[difference] === 'number') {
            return [indexByNumber[difference], i];
        }
        indexByNumber[number] = i;
    }
    return [-1, -1];
}
;
var resultTuple = twoSum(input, 2020);
var inputTuple = [input[resultTuple[0]], input[resultTuple[1]]];
console.log("Result TUPLE is " + inputTuple[0] + " " + inputTuple[1]);
// multiply
var resultMultiply = inputTuple[0] * inputTuple[1];
// print result
console.log("Result AMOUNT is " + resultMultiply);
