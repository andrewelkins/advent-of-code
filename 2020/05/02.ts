console.log("2020 - 05 - Part 1")
const fs = require('fs');

// Read input
var input: Array<string> = fs.readFileSync(__dirname + '/input.txt', 'utf8').toString().split('\n');

let highest_id:number = 0;
let id_list:Array<number> = [];

function reduceList(input_list, half_type) {
  const half = Math.ceil(input_list.length / 2);
  if(half_type == 'F' || half_type == 'L'){
    return input_list.splice(0, half);
  } else if(half_type == 'B' || half_type == 'R'){
    return input_list.splice(-half);
  }
}

// Row loop
for (var i = 0; i < (input.length-1); i++) {
  let range_list = [...Array.from(Array(128).keys())];
  // element loop
  for (var x = 0; x < 7; x++) {
    range_list = reduceList(range_list, input[i][x]);
  }
  let column_list = [...Array.from(Array(8).keys())];
  for (var x = 7; x < input[i].length; x++) {
    column_list = reduceList(column_list, input[i][x])
  }

  let current_id = Number.parseInt(range_list) * 8 + Number.parseInt(column_list);
  id_list.push(current_id);
  if (current_id > highest_id) {
    highest_id = current_id;
  }
}

console.log(highest_id)
// id_list.sort();
id_list.sort(function(a, b) {
  return a - b;
});
for (var i = 6; i < (id_list.length); i++) {
  if(id_list[i-1] !== id_list[i]-1 || id_list[i+1] !== id_list[i]+1){
    console.log(id_list[i]+1)
    break;
  }
}
