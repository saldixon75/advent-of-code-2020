import numpy;
import sys;

with open("input.txt") as f:
    rows = f.read().splitlines();

current_layout = [];
r=0;
for row in rows:
    current_layout.append(list(row));

number_of_rows = len(current_layout);
number_of_columns = len(list(current_layout[0]));

print("number_of_rows=" + str(number_of_rows) + " number_of_columns=" + str(number_of_columns) );

def is_seat(slot):
    if (slot == '#' or slot == 'L'):
        return True;
    return False;   

def get_nearest_seats(r,c):
    # actually, it's the nearest seat in each of the eight directions that we need to find
    directions = [[-1,-1], [-1,0], [-1,1], [0,-1], [0,1], [1,-1], [1,0], [1,1]];

    neighbours = [];
    for direction in directions:
  #      print("DIRECTION!!!" + str(direction));
        current_slot = [r,c];
        nearest_seat = [];
        while len(nearest_seat) == 0:
 #           print("current_slot = " + str(current_slot) + " direction = " + str(direction));
            next_slot = [current_slot[0] + direction[0],current_slot[1] + direction[1]]; 
#            print("next_slot = " + str(next_slot));
            if (next_slot[0] <0 or next_slot[0] >= number_of_rows or next_slot[1] <0 or next_slot[1] >= number_of_columns):
                break; # we have gone out of bounds, and still not found a seat in this direction
            if (is_seat(current_layout[next_slot[0]][next_slot[1]])):
                nearest_seat = next_slot;
                neighbours.append(nearest_seat);
            current_slot = next_slot;    
    return neighbours;


def get_neighbours_states(neighbours):
    states = [];
    for neighbour in neighbours:
        state = current_layout[neighbour[0]][neighbour[1]];
        states.append(state);
    return states;

def is_occupied(seat):
    if (seat == '#'):
        return True;
    return False;    

def get_next_state(current_state, number_of_occupied_neighbours):
    if (current_state == 'L' and number_of_occupied_neighbours == 0):
        # seat becomes occupied
        return '#';
    if(current_state == '#' and number_of_occupied_neighbours >= 5):
        return 'L';
    return current_state;    

def apply_seat_rules(current_layout):
    next_layout = [];
    for row in range(0,number_of_rows):
        next_row=[];
        for col in range(0,number_of_columns):
            #print("Looking at cell " + str(row) + "," + str(col));
            current_state = current_layout[row][col];
            nearest_seats = get_nearest_seats(row,col);
            #print(neighbours);
            neighbours_states = get_neighbours_states(nearest_seats);
            #print("neighbours states are .." + str(neighbours_states));
            number_of_occupied_neighbours = len(filter(is_occupied, neighbours_states));
            #print("current_state = " + current_state + ", number_of_occupied_neighbours=" + str(number_of_occupied_neighbours));
            next_state = get_next_state(current_state,number_of_occupied_neighbours);
            next_row.append(next_state);
        next_layout.append(next_row);
    return next_layout;

def how_many_seats_occupied(layout):
    counter = 0;
    for row in layout:
        for col in row:
            if (is_occupied(col)):
                counter += 1;
    return counter;


#for i in range(8):    
while True:    
    #print("Applying seta rules: round" + str(i));
    next_layout = apply_seat_rules(current_layout);
    if(current_layout == next_layout):
        print("IT HAS STOPPED CHANGING!");
        # how many occupied seats?
        print("NUMBER OF SEATS OCCUPIED = " + str(how_many_seats_occupied(current_layout)));
        break;
    current_layout = next_layout[:] ;

#print(str(get_neighbours(0,3)));   




