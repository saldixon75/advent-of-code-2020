import sys;
import re;

f = open("input.txt", "r")

contents = f.read();
# passports are separated by blank lines

passports = contents.split("\n\n");

compulsory_fields = ["ecl","byr","iyr","eyr","hgt","hcl","ecl","pid"];

def has_field(passport, fieldname):
    print("checking " + passport + " for this field: " + field);

for passport in passports:
    #print("passport is: \n" + passport);
    valid = True;
    for field in compulsory_fields:
        if (not field in passport):
            valid = False;
            break;
    if (valid):
        print "passport is VALID"
    else:
        print "passport is INVALID"


