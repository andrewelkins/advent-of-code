console.log("2020 - 03 - Part 1")
const fs = require('fs');

// Read input
var input: Array<string> = fs.readFileSync(__dirname + '/input.txt', 'utf8').toString().split('\n');

// (line width / 3) * length = multiplier
let multiplier:number = Math.round((32/3)*input.length);

// loop through lines tracking position.
let tree_count: number = 0;
let current_position: number = 0;

for (var i = 1; i < input.length; i++) {
    let current_row: string = input[i].repeat(multiplier);
    current_position += 3
    current_status = current_row[current_position];
    if(current_status == '#') {
      tree_count += 1;
    }
}

console.log(`Tree count: ${tree_count}`);
