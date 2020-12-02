console.log("2020 - 02 - Part 1");
var fs = require('fs');
// Read input
var input = fs.readFileSync(__dirname + '/input.txt', 'utf8').toString().split('\n');
var count = 0;
for (var i = 0; i < input.length; i++) {
    var current_process = input[i].split(' ');
    if (current_process.length == 3) {
        var range = current_process[0].split('-');
        var low_range = parseInt(range[0]);
        var high_range = parseInt(range[1]);
        var sight = current_process[1].substring(0, current_process[1].length - 1);
        var value = current_process[2];
        var current_count = value.split(sight).length - 1;
        if (current_count >= low_range && current_count <= high_range) {
            count += 1;
        }
    }
}
console.log(count);
