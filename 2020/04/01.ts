console.log("2020 - 04 - Part 1")
const fs = require('fs');

// Read input
var input: Array<string> = fs.readFileSync(__dirname + '/input.txt', 'utf8').toString().split('\n');

let current_passport: string = '';
let passport_count: number = 0;
const passport_field = [
    'byr', //(Birth Year)
    'iyr', //(Issue Year)
    'eyr', //(Expiration Year)
    'hgt', //(Height)
    'hcl', //(Hair Color)
    'ecl', //(Eye Color)
    'pid', //(Passport ID)
    'cid', //(Country ID)
]

for (var i = 0; i < input.length; i++) {
    if (input[i] == '') {
      let data: any = current_passport.trim().split(' ');
      // Has to have at least 7 to have all fields except cid
      if (data.length >= 7) {
        let data_fields: Array<string> = []
        for(var x=0; x < data.length; x++) {
          data_fields.push(data[x].split(':')[0]);
        }
        const data_difference: Array<string> = passport_field.filter(x => data_fields.indexOf(x) === -1);
        if(data_difference.length <= 1 ) {
          if(data_difference.length == 1){
            if(data_difference[0] != 'cid'){
              current_passport = '';
              continue;
            }
          }
          passport_count++;
        }
      }

      current_passport = '';
    } else {
      current_passport += ' ' + input[i];
    }
}

console.log(passport_count);
console.log('== MAKE SURE THE INPUT HAS A TRAILING EMPTY LINE ==')
