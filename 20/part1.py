import numpy;
import sys;
import copy;
import re;


#  to reverse a string:  txt = "Hello World" [::-1]


with open("input.txt") as f:
    input = f.read();
    
tiles = input.split("\n\n");

print('There are ' + str(len(tiles)) + ' tiles' );

tiles_by_id = {};
tiles_by_edge = {};

def catalogue_edge(edge, id):
    global tiles_by_edge;
    if (edge in tiles_by_edge):
        tiles_by_edge[edge].append(id);
        tiles_by_edge[edge[::-1]].append(id);
    else:
        tiles_by_edge[edge] = [id];
        tiles_by_edge[edge[::-1]] = [id];

for tile in tiles:
    print(tile);
    lines = filter(lambda x: len(x)>0, tile.split('\n'));
    print('There are ' + str(len(lines)) + ' lines' );
    id = re.match('Tile (\d+):',lines[0]).groups()[0];
    lines.pop(0);
    top_edge = lines[0];
    bottom_edge = lines[9];
    bottom_edge = bottom_edge[::-1];
    left_edge_array = [];
    right_edge_array = [];
    for line in lines:
        right_edge_array.append(line[9]); # the last character
        left_edge_array.append(line[0]);
    left_edge_array.reverse();
    left_edge = ''.join(left_edge_array);
    right_edge = ''.join(right_edge_array);
    print("Tile id = " + str(id) + ' edges are ...');
    print(top_edge);     
    print(right_edge);     
    print(bottom_edge);     
    print(left_edge); 
    
    # print('Reversed edges are ...');

    catalogue_edge(top_edge,id);
    catalogue_edge(left_edge,id);
    catalogue_edge(bottom_edge,id);
    catalogue_edge(right_edge,id);

print(tiles_by_id);
print(tiles_by_edge);

#  now see if there are any edges that occur only once in the matrix. thee indicate corner ones.

for edge in tiles_by_edge.keys():
    print(edge + ' : ' + str(tiles_by_edge[edge]) );
    if (len(tiles_by_edge[edge]) < 2):
        # print('OUTSIDE EDGE!! tile id = ' + str(tiles_by_edge[edge]));
        if id in tiles_by_id:
            tiles_by_id[id].append(tile);
        else:
            tiles_by_id[id] = [tile];

# now tiles_by_id list the outside edges for a tile
for tile in tiles_by_id:
    if ( len(tiles_by_id[tile]) > 1 ): 
        print('CORNER PIECE!!!! id=' + tile);