import sys;
import re;

f = open("input.txt", "r")

lines = f.readlines();
lines = map(str.strip, lines);
col=1;
trees=0;

for line in lines:
    colToUse = col%31;
    #print line;
    if (colToUse == 0):
        print line + " col=" + str(col);
        colToUse = 31;
    char = line[colToUse-1];
    print "col number to use = " + str(colToUse) + ", char=" + char;
    if (char == '#'): 
        trees = trees+1; 
    col = col+3;

print "total trees = " + str(trees);
