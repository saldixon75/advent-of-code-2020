import logging, sys
import re;
import time;

logging.basicConfig(stream=sys.stderr, level=logging.INFO)
start = time.time();

def get_age(number_history):
    logging.debug('in get_age. number_history = %s', number_history);
    if (len(number_history) == 1):
        return 0;
    recent_history = number_history[-2:];     
    return (recent_history[1] - recent_history[0] );

starting_numbers = [0,3,6];
turn = len(starting_numbers) + 1;

spoken_numbers_by_number = {};
for i in range(len(starting_numbers)):
    spoken_numbers_by_number[starting_numbers[i]] = [i+1];

previous_number = starting_numbers[-1];
logging.info('About to start. turn = %d, previous number = %d', turn, previous_number);

while (turn < 2021): 
    logging.debug('Starting turn  %d ..previous number = %d. about to get age.', turn, previous_number);
    number = get_age(spoken_numbers_by_number[previous_number]);
    logging.info('TURN = %d number spoken this turn is %d', turn, number);
    
    # now add it to teh records..
    if( not number in spoken_numbers_by_number ) :
        spoken_numbers_by_number[number] = [turn];
    else:
        history = spoken_numbers_by_number[number];
        history.append(turn);
        spoken_numbers_by_number[number] = history;     
    previous_number = number;  
    turn += 1;
    logging.debug('complete record = %s', spoken_numbers_by_number);


end = time.time();
elapsed = end - start;

logging.debug('spoken numbers =  %s ', spoken_numbers_by_number);
logging.info('2020th number =  %d (in %d +  seconds)', number, elapsed);













