console.log("2020 - 03 - Part 1");
var fs = require('fs');
// Read input
var input = fs.readFileSync(__dirname + '/input.txt', 'utf8').toString().split('\n');
// total lines / (line width / 4) = multiplier
var multiplier = Math.round((32 / 3) * input.length);
// loop through lines tracking position.
var tree_count = 0;
var current_position = 0;
for (var i = 1; i < input.length; i++) {
    var current_row = input[i].repeat(multiplier);
    current_position += 3;
    current_status = current_row[current_position];
    if (current_status == '#') {
        tree_count += 1;
    }
}
console.log("Tree count: " + tree_count);
