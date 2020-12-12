import sys;
import re;

amended_lines = set([]);
rogue_line = 0;

with open("input.txt") as f:
    lines = f.read().splitlines();

def run_it(line_to_fix):
    global rogue_line;
    #print("Running it with line_to_fix = " + str(line_to_fix)); 
    accumulator = 0;
    visited_lines = set([]);
    line_number = 1;
    while True:
        #print("processing line " + str(line_number));
        if(line_number == 649):
            print("Woohoo!!  Got to teh end of the program! Accumulator = " + str(accumulator));
            rogue_line = line_to_fix;
            break;
        if (line_number in visited_lines):
            #print("ATTENTION!  WE HAVE BEEN HERE BEFORE! LINE NUMBER = " + str(line_number) + " accumulator = " + str(accumulator));   
            break;
        visited_lines.add(line_number);
        line = lines[line_number-1];   
        #print("line = " + line);
        match = re.match('(\w{3}) ([+-]\d+)',line);
        instruction = match.group(1);
        amount  = match.group(2);
        #print("instruction = " + instruction + " amount = " + amount);
        
        if (line_number == line_to_fix):
            if(instruction == 'jmp'):   
                instruction = 'nop'; 
            elif(instruction == 'nop'):   
                instruction = 'jmp'; 
        
        if(instruction == 'acc'):   
            accumulator = accumulator + int(amount);
            line_number += 1;
            continue;
        if(instruction == 'jmp'):   
            line_number = line_number + int(amount);
            continue;
        line_number += 1;



for i in range(len(lines)):
    if (rogue_line > 0 ):
        print("HEYYYYYY! THE ROGUE LINE IS " + str(rogue_line) );
        break;
    run_it(i+1);

