console.log("2020 - 02 - Part 1")
const fs = require('fs');

// Read input
var input: Array<string> = fs.readFileSync(__dirname + '/input.txt', 'utf8').toString().split('\n');

let count: number = 0;

for (let i = 0; i < input.length; i++) {
  const current_process = input[i].split(' ');
  if (current_process.length == 3) {
    const range: Array<any> = current_process[0].split('-');
    const low_range: number = parseInt(range[0]);
    const high_range: number = parseInt(range[1]);
    const sight: string = current_process[1].substring(0, current_process[1].length-1);
    const value: string = current_process[2];
    const current_count: number = value.split(sight).length - 1;
    if (current_count >= low_range && current_count <= high_range ) {
      count += 1;
    }
  }
}

console.log(count)
