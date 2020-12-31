import numpy;
import sys;
import copy;
import re;

with open("input.txt") as f:
    lines = f.read().splitlines();
    
def parse_line(line):
    moves = list();
    while len(line) > 0:
        if (line[0] in ('e','w')): 
            move = line[0];
            line = line[1:];
        else:
            move = line[0:2];
            line = line[2:];
        moves.append(move);        
    return moves;

def do_moves(moves):
    (x,y) = (0,0);
    for move in moves:
        if (move == 'e'):
            x += 2;
            continue;
        if (move == 'w'):
            x -= 2;
            continue;
        if (move[0] == 'n'):
            y += 1;
        if (move[0] == 's'):
            y -= 1;
        if (move [1] == 'e'):
            x += 1;
        if (move [1] == 'w'):
            x -= 1;
    # print('pos = ' + str(x) + ',' + str(y));
    return (x,y);


black_tiles = set();
for line in lines:
    moves = parse_line(line);
    position = do_moves(moves);
    if position in black_tiles:
        black_tiles.remove(position);
    else:    
        black_tiles.add(position);


print('all the black_tiles: ' + str(black_tiles));
print('Number of black_tiles: ' + str(len(black_tiles)));

#  now do a game of life thing...

# def get_neighbours(x,y):
def get_neighbours(tile_pos):
    x = tile_pos[0];
    y = tile_pos[1];
    return [
        (x-2,y),
        (x-1,y+1),
        (x+1,y+1),
        (x+2,y),
        (x+1,y-1),
        (x-1,y-1)
    ];


def get_next_state(current_state, tile):
    black_neighbours = 0;
    neighbours = get_neighbours(tile);
    for neighbour in neighbours:    
        if neighbour in black_tiles:
            black_neighbours += 1;
    if current_state == 'white' and black_neighbours==2:
        return 'black';
    if current_state == 'black' and (black_neighbours<1 or black_neighbours>2):
        return 'white';
    return current_state;

def apply_tile_rules(black_tiles):
    new_layout = set();
    #  we'll need to do all the balck tiles, but also all the white tiles which are next to them
    for black_tile in black_tiles:
        next_state = get_next_state('black',black_tile);
        if (next_state == 'black'):
            new_layout.add(black_tile);
        neighbours = get_neighbours(black_tile);
        for neighbour in neighbours:
            current_state = 'white';
            if (neighbour in black_tiles):
                current_state = 'black';
            next_state = get_next_state(current_state, neighbour);
            if (next_state == 'black'):
                new_layout.add(neighbour);  
    print('new layout number of balcks = ' + str(len(new_layout)));              
    return new_layout;


for i in range(100):   
    black_tiles = apply_tile_rules(black_tiles);

print('End state.. number of blakc tiles = ' + str(len(black_tiles)));



