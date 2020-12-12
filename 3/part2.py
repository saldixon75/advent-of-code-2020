import sys;
import re;

f = open("input.txt", "r")

lines = f.readlines();
lines = map(str.strip, lines);
col=1;
trees=0;
row = 1;

for line in lines:
    if (row%2 == 1): 
        colToUse = col%31;
        if (colToUse == 0):
            colToUse = 31;
        char = line[colToUse-1];
        if (char == '#'): 
            trees = trees+1; 
        col = col+1;
    row = row+1;


print "total trees 7,1 = " + str(trees);
