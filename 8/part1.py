import sys;
import re;

with open("input.txt") as f:
    lines = f.read().splitlines();

accumulator = 0;
visited_lines = set([]);
line_number = 1;

while True:
    #print("processing line " + str(line_number));
    if (line_number in visited_lines):
        print("ATTENTION!  WE HAVE BEEN HERE BEFORE! LINE NUMBER = " + str(line_number) + " accumulator = " + str(accumulator));   
        break;
    visited_lines.add(line_number);
    line = lines[line_number-1];   
    #print("line = " + line);
    match = re.match('(\w{3}) ([+-]\d+)',line);
    instruction = match.group(1);
    amount  = match.group(2);
    #print("instruction = " + instruction + " amount = " + amount);
    
    if(instruction == 'acc'):   
        accumulator = accumulator + int(amount);
        line_number += 1;
        continue;
    if(instruction == 'jmp'):   
        line_number = line_number + int(amount);
        continue;
    line_number += 1;


