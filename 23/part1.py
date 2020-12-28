import numpy;
import sys;
import copy;
import re;


# cups='389125467';
cups='789465123';


def get_destination(current_cup, candidates):
    candidate = int(current_cup);
    while ( not str(candidate) in list(candidates) ):
        candidate = candidate - 1;
        if (candidate == 0):
            candidate = 9;
    return candidate;    

def do_a_round(cups):
    current_cup = cups[0];
    print('Current cup = ' + current_cup + ', cups = ' + str(cups));
    #  get the next three cups
    three_to_move = cups[1:4];
    remainder = cups[4:];
    print('three_to_move = ' + three_to_move + ', remainder = ' + remainder);
    dest = str(get_destination(current_cup, remainder));
    print('dest = ' + str(dest));

    #  now stick em in...
    (pre, dest, post) = remainder.partition(dest);
    print('pre =' + pre + ' dest = ' + dest + ' post=' + post);
    new_cups = pre + dest + three_to_move + post + current_cup;  # currnet cup gets moved to the back
    return new_cups;


for i in range(100):
    cups = do_a_round(cups);

print('Now cups = ' + cups);
bits = cups.partition('1');
final_order = bits[2] + bits[0];
print('final order = ' + str(final_order));



