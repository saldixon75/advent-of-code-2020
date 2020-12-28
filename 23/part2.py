import numpy;
import sys;
import copy;
import re;

cupstring='389125467';
# cupstring='789465123';
#  need to use a list instead of a string 
cups=map(int,list(cupstring));


def get_destination(current_cup, candidates):
    candidate = current_cup;
    while ( not candidate in candidates ):
        candidate = candidate - 1;
        if (candidate == 0):
            print('Having to go to the highest one now!');
            candidate = 9; # todo fix this so it is dynamic
    return candidate;    

def do_a_round(cups):
    current_cup = cups.pop(0);
    print('Current cup = ' + str(current_cup) + ', cups = ' + str(cups));
    #  get the next three cups
    three_to_move = cups[0:3];
    remainder = cups[3:];
    # print('three_to_move = ' + str(three_to_move) + ', remainder = ' + str(remainder));
    dest = get_destination(current_cup, remainder);
    # print('dest = ' + str(dest));

    #  now stick em in...
    destination_pos = remainder.index(dest);
    # print('destination_pos = ' + str(destination_pos));
    pre = remainder[:destination_pos];
    post = remainder[destination_pos+1:];

    # print('pre =' + str(pre) + ' dest = ' + str(dest) + ' post=' + str(post));
    new_cups = pre + [dest] + three_to_move + post + [current_cup];  # currnet cup gets moved to the back

    # finally, stick the current_cup at the end
    # new_cups.append(current_cup);
    return new_cups;


for i in range(100):
    cups = do_a_round(cups);

print('Now cups = ' + str(cups));
location_of_one = cups.index(1);
# print('location_of_one = ' + str(location_of_one));

final_order = cups[location_of_one+1:] + cups[:location_of_one];
print('final order = ' + str(final_order));



