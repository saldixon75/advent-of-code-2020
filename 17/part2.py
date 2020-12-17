import numpy;
import sys;

with open("input.txt") as f:
    rows = f.read().splitlines();

gridsize = len(rows);
#  start the co-ordinate system at the top left of the initial 2D grid provided
current_layout = {};

for r in range(gridsize):
    cols = list(rows[r]);
    for c in range(len(cols)):
        current_layout["{}:{}:0:0".format(c,r)] = cols[c];

print("Starting layout is ...");
print(current_layout);

# def get_neighbours(x,y,z):
def get_neighbours(location_key):
    coords = map(int,location_key.split(':'));
    x = coords[0];
    y = coords[1];
    z = coords[2];
    w = coords[3];
    neighbours = [];
    for i in range(-1,2):
        for j in range(-1,2):
            for k in range(-1,2):
                for l in range(-1,2):
                    neighbours.append("{}:{}:{}:{}".format(str(x+i),str(y+j),str(z+k),str(w+l)));
    neighbours.remove("{}:{}:{}:{}".format(x,y,z,w));
    return neighbours;

def get_number_of_active_neighbours(neighbours):
    running_total = 0;
    for n in neighbours:
        if n in current_layout:
            state = current_layout[n];
        else:
            state = '.';    
        
        if (state == '#'):
            running_total += 1;
    return running_total;

def get_next_state(current_state, number_of_active_neighbours):
    if (current_state == '#'):
        if ((number_of_active_neighbours < 2)  or ( number_of_active_neighbours >3)):
            return '.';   #it dies
    else:
        if ( number_of_active_neighbours == 3 ):
            return '#'; # comes to life
    return current_state; # no change    

def apply_cycle_rules(current_layout):
    next_layout = {};
    for cube_location in current_layout.keys():
        current_state = current_layout[cube_location];
        neighbours = get_neighbours(cube_location);
        # print('number of neighbours is .. ' + str(len(neighbours)));
        number_of_active_neighbours = get_number_of_active_neighbours(neighbours);
        # print("number_of_active_neighbours=" + str(number_of_active_neighbours));
        next_state = get_next_state(current_state,number_of_active_neighbours);
        next_layout[cube_location] = next_state;
        #  now what about all those neighbours?  if they are already in the current universe, don't worry.
        #  if there are NOT currently mapped, we need to add them...
        for n in neighbours:
            if ((n in current_layout) or (n in next_layout)):
                #  already taken care of. do nowt.
                continue;
            n_neighbours = get_neighbours(n);
            number_of_active_n_neighbours = get_number_of_active_neighbours(n_neighbours);
            next_state = get_next_state(current_state,number_of_active_n_neighbours);
            next_layout[n] = next_state;
    return next_layout;

def get_total_active(layout):
    count = len(filter(lambda x: x == '#', layout.values()));
    return count;

for i in range(6):    
    next_layout = apply_cycle_rules(current_layout);
    number_active = get_total_active(next_layout);
    print("i= " + str(i) + " How many active? = " + str(number_active));
    current_layout = next_layout.copy() ;




