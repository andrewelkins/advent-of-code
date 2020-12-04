console.log("2020 - 04 - Part 1");
var fs = require('fs');
// Read input
var input = fs.readFileSync(__dirname + '/input.txt', 'utf8').toString().split('\n');
var current_passport = '';
var passport_count = 0;
var passport_field = [
    'byr',
    'iyr',
    'eyr',
    'hgt',
    'hcl',
    'ecl',
    'pid',
    'cid',
];
var _loop_1 = function () {
    if (input[i] == '') {
        var data = current_passport.trim().split(' ');
        // Has to have all fields except cid
        if (data.length >= 7) {
            var data_fields_1 = [];
            for (var x = 0; x < data.length; x++) {
                data_fields_1.push(data[x].split(':')[0]);
            }
            var data_difference = passport_field.filter(function (x) { return data_fields_1.indexOf(x) === -1; });
            if (data_difference.length <= 1) {
                if (data_difference.length == 1) {
                    if (data_difference[0] != 'cid') {
                        current_passport = '';
                        return "continue";
                    }
                }
                passport_count++;
            }
        }
        current_passport = '';
    }
    else {
        current_passport += ' ' + input[i];
    }
};
for (var i = 0; i < input.length; i++) {
    _loop_1();
}
console.log(passport_count);
console.log('== MAKE SURE THE INPUT HAS A TRAILING EMPTY LINE ==');
