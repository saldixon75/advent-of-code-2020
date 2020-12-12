import numpy;
import sys;
import re;

with open("input.txt") as f:
    instructions = f.read().splitlines();

#compass_directions = {'N':0,'S':180,'E':90,'W':270};
compass_directions = {0:'N',90:'E',180:'S',270:'W'};
current_position = [0,0];
facing = 90;

def get_manhattan_distance(pos):
    return abs(pos[0]) + abs(pos[1]);

def apply_instruction(instr,amount,current_pos):
    global facing; # yuck
    if (instr == 'N'):
        return([current_pos[0], current_pos[1]+amount]);
    if (instr == 'S'):
        return([ current_pos[0], current_pos[1]-amount ]);
    if (instr == 'E'):
        return([current_pos[0]+amount, current_pos[1]]);
    if (instr == 'W'):
        return([current_pos[0]-amount, current_pos[1]]);   

    if (instr == 'F'):
        return apply_instruction(compass_directions[facing],amount,current_pos);

    if (instr == 'L'):
        facing = (facing - amount)%360;
        return current_pos;
        
    if (instr == 'R'):
        facing = (facing + amount)%360;
        return current_pos;



for instruction in instructions:
    matches = re.match('(\w)(\d+)',instruction);
    instr = matches.groups()[0];
    amount = int(matches.groups()[1]);
    print("curreny_pos = " + str(current_position) + ", instr=" + instr + ", amount = " + str(amount));
    current_position = apply_instruction(instr,amount, current_position);

print("Position after all the moves is..." + str(current_position));
print("Manhattan distnace..." + str(get_manhattan_distance(current_position)));











