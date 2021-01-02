import sys;
import copy;
import re;


#  to reverse a string:  txt = "Hello World" [::-1]


with open("input.txt") as f:
    input = f.read();
    
tiles = input.split("\n\n");

print('There are ' + str(len(tiles)) + ' tiles' );

outside_edges_by_tile_id = {};
tiles_by_edge = {};

def catalogue_edge(edge, id):
    global tiles_by_edge;
    if (edge in tiles_by_edge):
        tiles_by_edge[edge].append(id);
        tiles_by_edge[edge[::-1]].append(id+'-flipped');
    else:
        tiles_by_edge[edge] = [id];
        tiles_by_edge[edge[::-1]] = [id+'-flipped'];

for tile in tiles:
    # print(tile);
    lines = list(filter(lambda x: len(x)>0, tile.split('\n')));
    # print('There are ' + str(len(lines)) + ' lines' );
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
    # print("Tile id = " + str(id) + ' edges are ...');
    # print(top_edge);     
    # print(right_edge);     
    # print(bottom_edge);     
    # print(left_edge); 
    
    # print('Reversed edges are ...');

    catalogue_edge(top_edge,id);
    catalogue_edge(left_edge,id);
    catalogue_edge(bottom_edge,id);
    catalogue_edge(right_edge,id);

# print(tiles_by_edge);

#  now see if there are any edges that occur only once in the matrix. 

for edge in tiles_by_edge.keys():
    # print(edge + ' : ' + str(tiles_by_edge[edge]) );
    if (len(tiles_by_edge[edge]) < 2):
        tile_id = tiles_by_edge[edge][0];
        # print('OUTSIDE EDGE!! edge = ' + edge + '  tile id = ' + str(tile_id));
        if tile_id in outside_edges_by_tile_id:
            outside_edges_by_tile_id[tile_id].append(edge);
        else:
            outside_edges_by_tile_id[tile_id] = [edge];

# print(outside_edges_by_tile_id);

# now tiles_by_id list the outside edges for a tile
for tile in outside_edges_by_tile_id:
    if ( len(outside_edges_by_tile_id[tile]) > 1 ): 
        print('CORNER PIECE!!!! id=' + tile);


#  need to assemble the tiles... having found teh corner pieces.. we will have to figure out where all the others go.


