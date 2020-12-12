import sys;
import re;

f = open("input.txt", "r")

contents = f.read();
# passports are separated by blank lines

passports = contents.split("\n\n");

compulsory_fields = ["byr","iyr","eyr","hgt","hcl","ecl","pid"];

def byro(val):
    return re.match("\d{4}$",val) and int(val) >= 1920 and int(val) <= 2002;

def iyr(val):
    return re.match("\d{4}$",val) and int(val) >= 2010 and int(val) <= 2020;

def eyr(val):
    return re.match("\d{4}$",val) and int(val) >= 2020 and int(val) <= 2030;

def hgt(val):
    matchy = re.search("(\d+)(cm|in)",val);
    #print(matchy.group(0));
    if (not matchy):
        return False; 
    height = int(matchy.group(1));
    if (matchy.group(2) == 'cm'):
        return height >= 150 and height <= 193;
    else:
        return height >= 59 and height <= 76;
   

def hcl(val):
    return re.match("#[a-f0-9]{6}$",val);

def ecl(val):
    return re.match("(amb|blu|brn|gry|grn|hzl|oth)$",val);

def pid(val):
    return re.match("\d{9}$",val);

print("byro = " +  str(hcl('#1915')));

validator = {
    'byr': byro,
    'iyr': iyr,
    'eyr': eyr,
    'hcl': hcl,
    'ecl': ecl,
    'pid': pid,
    'hgt': hgt,
}


def is_valid(passport, fieldname):
    print("checking " + passport + " for this field: " + fieldname);
    reggie = fieldname + ':([^\s]+)';  
    val = re.search(reggie, passport);
    if (val):
        print("EXTRACTED! " + val.group(1));
    else:
        print("not found");
        return False;
    val = val.group(1);
    #print(str(validator.get(fieldname)(val)));
    return validator.get(fieldname)(val);

for passport in passports:
    #print("passport is: \n" + passport);
    valid = True;
    

    for field in compulsory_fields:
        if (not field in passport):
            valid = False;
            break;
        if (not is_valid(passport, field)):
            valid = False;
            break;
    if (valid):
        print "passport is VALID"
    else:
        print "passport is INVALID"


