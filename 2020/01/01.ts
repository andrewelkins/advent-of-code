console.log("2020 - 01 - Part 1")
const fs = require('fs');

// Read input
var input = fs.readFileSync(__dirname + '/input.txt', 'utf8').toString().split('\n');

function twoSum(inputs: Array<number>, target: number) {
  const indexByNumber = {};

  for (let i = 0; i < inputs.length; i++) {
    const number = inputs[i];
    const difference = target - number;

    if (typeof indexByNumber[difference] === 'number') {
      return [indexByNumber[difference], i];
    }
    indexByNumber[number] = i;
  }

  return [-1, -1];
};

const resultTuple: Array<number> = twoSum(input, 2020);
const inputTuple: Array<number> = [input[resultTuple[0]], input[resultTuple[1]]]
console.log(`Result TUPLE is ${inputTuple[0]} ${inputTuple[1]}`);
// multiply
const resultMultiply: number = inputTuple[0] * inputTuple[1];

// print result
console.log(`Result AMOUNT is ${resultMultiply}`);
