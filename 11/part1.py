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
#print("Current layout is ...");
#print(current_layout);

def get_neighbours(r,c):
    neighbour_rows = [r-1,r,r+1]; 
    neighbour_cols = [c-1,c,c+1];
    neighbours = [];
    for nrow in neighbour_rows:
        if ( (nrow < 0) or (nrow >= number_of_rows) ):
            continue;
        for ncol in neighbour_cols:
            if (ncol<0 or ncol >= number_of_columns or (nrow == r and ncol == c)):
                continue;
            neighbours.append( [ nrow,ncol ] );
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
        #print("A change!  current_state = " + str(current_state) + " number_of_occupied_neighbours=" + str(number_of_occupied_neighbours));
        return '#';
    if(current_state == '#' and number_of_occupied_neighbours >= 4):
        return 'L';
        #print("A change!");
    return current_state;    

def apply_seat_rules(current_layout):
    next_layout = [];
    for row in range(0,number_of_rows):
        next_row=[];
        for col in range(0,number_of_columns):
            #print("Looking at cell " + str(row) + "," + str(col));
            current_state = current_layout[row][col];
            neighbours = get_neighbours(row,col);
            #print(neighbours);
            neighbours_states = get_neighbours_states(neighbours);
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
    #print("next_layout is ...");
    #print(next_layout);
    current_layout = next_layout[:] ;




