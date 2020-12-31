import numpy;
import sys;
import copy;
import re;


with open("input.txt") as f:
    lines = f.read().splitlines();
    

# line = 'neeswseenwwswnwswswnw';

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


flipped_tiles = {};
for line in lines:
    moves = parse_line(line);
    position = do_moves(moves);
    if position in flipped_tiles:
        flipped_tiles.pop(position);
    else:    
        flipped_tiles[position] = 1;


print('all the flipped tiles: ' + str(flipped_tiles));
print('Number of flipped tiles: ' + str(len(flipped_tiles.keys())));
