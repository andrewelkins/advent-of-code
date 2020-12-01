console.log("2020 - 01 - Part 1")
const fs = require('fs');

// const
const targetValue = 2020;

// Read input
var input = fs.readFileSync(__dirname + '/input.txt', 'utf8').toString().split('\n');

// parse through like 2-sum
function twoSum(inputs: Array<number>, target: number, topLevel: boolean = false) {
  const indexByNumber = {};

  for (let i = 0; i < inputs.length; i++) {
    const number_test = inputs[i];
    const difference = target - number_test;

    if(topLevel) {
      const tempDiff = twoSum(inputs, difference);
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
};

const resultTuple: Array<number> = twoSum(input, targetValue, true);
console.log(resultTuple);
const resultMultiply: number = resultTuple.reduce((a, b)=> parseInt(a)*parseInt(b), 1);

// print result
console.log(`Result AMOUNT is ${resultMultiply}`);
