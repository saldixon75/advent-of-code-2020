import sys;
import re;

f = open("input.txt", "r")

lines = f.readlines();
lines = map(str.strip, lines);
line_pattern = '(\d+)-(\d+) (\w): (\w+)';

for line in lines:
    x = re.search(line_pattern, line);
    pos1 = int(x.group(1));
    pos2 = int(x.group(2));
    letter = x.group(3);
    password = x.group(4);

    print line;
    if (password[pos1-1] == letter and password[pos2-1] == letter):
        print "FAILED! password = " + password + " letter = " + letter + " pos1=" + str(pos1) + ":" + password[pos1-1] + ", pos2=" + str(pos2) + ":" + password[pos2-1];
    elif (password[pos1-1] != letter and password[pos2-1] != letter):
        print "FAILED! password = " + password + " letter = " + letter + " pos1=" + str(pos1) + ":" + password[pos1-1] + ", pos2=" + str(pos2) + ":" + password[pos2-1];
    else:
        print "PASSED! " + password;
