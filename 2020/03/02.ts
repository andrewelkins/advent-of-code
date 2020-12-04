console.log("2020 - 03 - Part 2")
const fs = require('fs');

// Read input
var input: Array<string> = fs.readFileSync(__dirname + '/input.txt', 'utf8').toString().split('\n');

const nav_list = [
  [1,1],
  [3,1],
  [5,1],
  [7,1],
  [1,2],
];

let tree_count: Array<number> = [];

for (var t = 0; t < nav_list.length; t++) {
  tree_count[t] = 0;
  let x = nav_list[t][0];
  let y = nav_list[t][1];

  // (line width / x) * length = multiplier
  let multiplier:number = Math.round((32/x)*input.length);

  // loop through lines tracking position.
  let current_position: number = 0;

  for (var i=y; i < input.length; i+=y) {
      let current_row: string = input[i].repeat(multiplier);
      current_position += x
      let current_status: string = current_row[current_position];
      if(current_status == '#') {
        tree_count[t]++;
      }
  }
}

console.log(tree_count);
console.log(tree_count.reduce( (a, b) => a * b ));
