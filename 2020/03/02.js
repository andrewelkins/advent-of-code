console.log("2020 - 03 - Part 2");
var fs = require('fs');
// Read input
var input = fs.readFileSync(__dirname + '/input.txt', 'utf8').toString().split('\n');
var nav_list = [
    [1, 1],
    [3, 1],
    [5, 1],
    [7, 1],
    [1, 2],
];
var tree_count = [];
for (var t = 0; t < nav_list.length; t++) {
    tree_count[t] = 0;
    var x = nav_list[t][0];
    var y = nav_list[t][1];
    // (line width / x) * length = multiplier
    var multiplier = Math.round((32 / x) * input.length);
    // loop through lines tracking position.
    var current_position = 0;
    for (var i = y; i < input.length; i += y) {
        var current_row = input[i].repeat(multiplier);
        current_position += x;
        var current_status = current_row[current_position];
        if (current_status == '#') {
            tree_count[t]++;
        }
    }
}
console.log(tree_count);
console.log(tree_count.reduce(function (a, b) { return a * b; }));
