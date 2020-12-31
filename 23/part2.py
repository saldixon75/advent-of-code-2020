import numpy;
import sys;
import copy;
import re;
import time;

number_of_cups = 1000000;
moves_to_do = 1000;

number_of_cups = 9;
moves_to_do = 100;
cupstring='389125467';

cupstring='789465123';

cups=list(map(int,list(cupstring)));
#  add the extra cups
for i in range(len(cups)+1,number_of_cups+1):
    # print('appending');
    cups.append(i);

# print('cups are: ' + str(cups));
print('Number of cups: ' + str(len(cups)))

start = time.time();
print("Started at " + str(time.gmtime(start)));


def get_destination(current_cup, exempt):
    candidate = current_cup;
    while ( candidate in exempt + [current_cup] ):
        candidate = candidate - 1;
        if (candidate == 0):
            candidate = number_of_cups; 
    return candidate;  

def do_a_move(cups):
    current_cup = cups.pop(0);
    # print('Current cup = ' + str(current_cup));
    #  + ', cups = ' + str(cups));
    #  get the next three cups
    three_to_move = cups[0:3];
    # print('ccup = ' + str(current_cup) + ' trio=' + str(three_to_move));
    remainder = cups[3:];
    # print('three_to_move = ' + str(three_to_move) + ', remainder = ' + str(remainder));
    # print('three_to_move = ' + str(three_to_move));
    dest = get_destination(current_cup, three_to_move);
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


for i in range(moves_to_do):
    # if (i+1)%1000 == 0:
    if i%1000 == 0:
        print('Playing move ' + str(i+1));
        print('time taken so far = ' + str((time.time()-start)/60) + ' minutes');
    cups = do_a_move(cups);
    # print(cups);


# print('Now cups = ' + str(cups));
location_of_one = cups.index(1);
# print('location_of_one = ' + str(location_of_one));

final_order = cups[location_of_one+1:] + cups[:location_of_one];
first_one = final_order[0];
second_one = final_order[1];
print('first_one = ' + str(first_one) + ' second one = ' + str(second_one));
print('FINAL RESULT = ' + str(first_one*second_one));

end = time.time();
print("It took this many seconds: " + str(end-start));
print("It took this many minutes: " + str((end-start)/60));

if (len(cups)<1000):
    print('final order = ' + str(cups));


