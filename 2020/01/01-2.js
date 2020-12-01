console.log("2020 - 01 - Part 1");
var fs = require('fs');
// const
var targetValue = 2020;
// Read input
var input = fs.readFileSync(__dirname + '/input.txt', 'utf8').toString().split('\n');
// parse through like 2-sum
function twoSum(inputs, target, topLevel) {
    if (topLevel === void 0) { topLevel = false; }
    var indexByNumber = {};
    for (var i = 0; i < inputs.length; i++) {
        var number_test = inputs[i];
        var difference = target - number_test;
        if (topLevel) {
            var tempDiff = twoSum(inputs, difference);
            if (tempDiff[0] !== -1) {
                return [number_test, inputs[tempDiff[0]], inputs[tempDiff[1]]];
            }
        }
        if (typeof indexByNumber[difference] === 'number') {
            return [indexByNumber[difference], i];
        }
        indexByNumber[number_test] = i;
    }
    return [-1, -1];
}
;
var resultTuple = twoSum(input, targetValue, true);
console.log(resultTuple);
var resultMultiply = resultTuple.reduce(function (a, b) { return parseInt(a) * parseInt(b); }, 1);
// print result
console.log("Result AMOUNT is " + resultMultiply);
