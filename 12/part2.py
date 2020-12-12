import numpy;
import sys;
import re;

with open("input.txt") as f:
    instructions = f.read().splitlines();

ship_position = [0,0];
way_point = [10,1]; # 10 east, 1 north

def get_manhattan_distance(pos):
    return abs(pos[0]) + abs(pos[1]);

def move_it(vector,current_pos):
    new_pos = [current_pos[0] + vector[0], current_pos[1] + vector[1] ];
    return new_pos;

def apply_instruction(instr,amount,current_pos):
    if (instr == 'N'):
        return([current_pos[0], current_pos[1]+amount]);
    if (instr == 'S'):
        return([ current_pos[0], current_pos[1]-amount ]);
    if (instr == 'E'):
        return([current_pos[0]+amount, current_pos[1]]);
    if (instr == 'W'):
        return([current_pos[0]-amount, current_pos[1]]);   

    if (instr == 'L'):
        return apply_instruction('R',(-amount)%360,current_pos);
        
    if (instr == 'R'):
        if (amount == 90):
            return([current_pos[1], -current_pos[0]]);
        if (amount == 180):
            return([-current_pos[0], -current_pos[1]]);
        if (amount == 270):
            return([-current_pos[1], current_pos[0]]);


for instruction in instructions:
    matches = re.match('(\w)(\d+)',instruction);
    instr = matches.groups()[0];
    amount = int(matches.groups()[1]);
    print("shippos = " + str(ship_position) + ", way_point=" + str(way_point) + ", instr=" + instr + ", amount = " + str(amount));

    if(instr=='F'):
        # move the ship
        for i in range(amount):
            ship_position = move_it(ship_position, way_point);    
    else:
        way_point = apply_instruction(instr,amount,way_point);        
    

print("Position after all the moves is..." + str(ship_position));
print("Manhattan distnace..." + str(get_manhattan_distance(ship_position)));











