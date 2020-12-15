import logging, sys
import re;
import time;

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
start = time.time();

def get_age(recent_history):
    if (len(recent_history) == 1):
        return 0;
    return (recent_history[1] - recent_history[0] );

starting_numbers = [0,8,15,2,12,1,4];
turn = len(starting_numbers) + 1;

spoken_numbers_by_number = {};
for i in range(len(starting_numbers)):
    spoken_numbers_by_number[starting_numbers[i]] = [i+1];

previous_number = starting_numbers[-1];
logging.info('About to start. turn = %d, previous number = %d', turn, previous_number);

while (turn < 30000001): 
    number = get_age(spoken_numbers_by_number[previous_number]);
    #logging.info('TURN = %d number spoken this turn is %d', turn, number);
    print(str(turn));
    
    # now add it to teh records..
    if( not number in spoken_numbers_by_number ) :
        spoken_numbers_by_number[number] = [turn];
    else:
        updated_history = [spoken_numbers_by_number[number].pop(),turn];
        spoken_numbers_by_number[number] = updated_history;     
    previous_number = number;  
    turn += 1;


end = time.time();
elapsed = end - start;

logging.debug('spoken numbers =  %s ', spoken_numbers_by_number);
logging.info('2020th number =  %d (in %d +  seconds)', number, elapsed);













