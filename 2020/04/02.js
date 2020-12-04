console.log("2020 - 04 - Part 2");
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
        if (data.length >= 7 && !(new Set(data)).size !== data.length) {
            var data_fields_1 = [];
            var data_map = {};
            for (var x = 0; x < data.length; x++) {
                data_fields_1.push(data[x].split(':')[0].trim());
                data_map[data[x].split(':')[0].trim()] = data[x].split(':')[1].trim();
            }
            var data_difference = passport_field.filter(function (x) { return data_fields_1.indexOf(x) === -1; });
            if (data_difference.length <= 1) {
                if (data_difference.length == 1) {
                    if (data_difference[0] != 'cid') {
                        console.log(data_difference);
                        current_passport = '';
                        return "continue";
                    }
                }
                if (data_difference.length == 0 && data.length == 7) {
                    current_passport = '';
                    return "continue";
                }
                // data validation
                // byr (Birth Year) - four digits; at least 1920 and at most 2002.
                if (Number.parseInt(data_map['byr']) < 1920 || Number.parseInt(data_map['byr']) > 2002) {
                    current_passport = '';
                    return "continue";
                }
                // iyr (Issue Year) - four digits; at least 2010 and at most 2020.
                if (Number.parseInt(data_map['iyr']) < 2010 || Number.parseInt(data_map['iyr']) > 2020) {
                    current_passport = '';
                    return "continue";
                }
                // eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
                if (Number.parseInt(data_map['eyr']) < 2020 || Number.parseInt(data_map['eyr']) > 2030) {
                    current_passport = '';
                    return "continue";
                }
                // hgt (Height) - a number followed by either cm or in:
                // If cm, the number must be at least 150 and at most 193.
                // If in, the number must be at least 59 and at most 76.
                if (data_map['hgt'].indexOf('cm') !== -1) {
                    var t = data_map['hgt'].replace('cm', '');
                    if (Number.parseInt(t) < 150 || Number.parseInt(t) > 193) {
                        current_passport = '';
                        return "continue";
                    }
                }
                else if (data_map['hgt'].indexOf('in') !== -1) {
                    var t = data_map['hgt'].replace('in', '');
                    if (Number.parseInt(t) < 59 || Number.parseInt(t) > 76) {
                        current_passport = '';
                        return "continue";
                    }
                }
                else {
                    current_passport = '';
                    return "continue";
                }
                //
                // hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
                if (!/^#[0-9a-f]{6}$/i.test(data_map['hcl'])) {
                    current_passport = '';
                    return "continue";
                }
                // ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
                if (!/^(amb|blu|brn|gry|grn|hzl|oth)$/i.test(data_map['ecl'])) {
                    current_passport = '';
                    return "continue";
                }
                // pid (Passport ID) - a nine-digit number, including leading zeroes.
                if (!/^\d{9}$/i.test(data_map['pid'])) {
                    current_passport = '';
                    return "continue";
                }
                passport_count++;
            }
        }
        current_passport = '';
    }
    else {
        current_passport += input[i].trim() + ' ';
    }
};
for (var i = 0; i < input.length; i++) {
    _loop_1();
}
console.log(passport_count);
