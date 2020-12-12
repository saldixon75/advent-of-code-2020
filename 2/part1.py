import sys;
import re;

f = open("input.txt", "r")

lines = f.readlines();
lines = map(str.strip, lines);
line_pattern = '(\d+)-(\d+) (\w): (\w+)';

for line in lines:
    x = re.search(line_pattern, line);
    min_occurrences = int(x.group(1));
    max_occurrences = int(x.group(2));
    letter = x.group(3);
    password = x.group(4);
    print "Password rule: between " + str(min_occurrences) + " and " + str(max_occurrences) + " of the letter " + letter;
    #print "number of captured groups = " + str(len(x.groups()));
    #regex = letter + '?'; # needs to be non-greedy
    password_search = re.findall('('+letter+')',password); 
    actual_occurrences = len(password_search);
    #print "actual = " + str(actual_occurrences) + ", password = " + password;
    if (actual_occurrences < min_occurrences or actual_occurrences > max_occurrences):
        print "FAILED! " + password + ", actual = " + str(actual_occurrences);
    else:
        print "PASSED! " + password
