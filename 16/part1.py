import numpy;
import logging, sys
import re;
import time;

logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
start = time.time();

with open("input.txt") as f:
    fileparts = f.read().split("\n\n");

def parse_ticket(ticket):
    return map(int, ticket.split(','));

def parse_rule(rule):
    match = re.match('(.+): (\d+-\d+) or (\d+-\d+)', rule);
    valid_range_1 = map(int, match.group(2).split('-'));
    valid_range_2 = map(int, match.group(3).split('-'));
    # logging.debug(valid_range_1);
    return [valid_range_1, valid_range_2];

fieldrules = fileparts[0].split("\n");
myticket = parse_ticket(fileparts[1].split("\n")[1]);

nearbytickets = fileparts[2].split("\n");
nearbytickets.remove('');
nearbytickets.remove('nearby tickets:');
nearbytickets = map(parse_ticket, nearbytickets);

rules = [];
for fieldruleset in fieldrules:
    for rule in parse_rule(fieldruleset):
        rules.append(rule);
        
print("all rules = \n\n" + str(rules));

logging.info('my ticket = %s', myticket);
logging.info('nearby tickets = \n%s', nearbytickets);

def validate_ticket(ticket):
    #  ticket is simply a list of integers
    invalid_fields = [];
    for fieldvalue in ticket:
        # does it satisfy any of the rules?
        passes = False;
        for rule in rules:
            # print('apply rule ' + str(rule) + ' to ticket ' + str(fieldvalue) );
            if (fieldvalue >= rule[0] and fieldvalue <= rule[1]):
                passes = True;
                break;
        if (not passes):
            invalid_fields.append(fieldvalue);        
    return invalid_fields;
    #  return a list of invalid numbers

invalid_fieldvals = [];

for ticket in nearbytickets:
    invalid_ticketvals = validate_ticket(ticket);
    for val in invalid_ticketvals:
        invalid_fieldvals.append(val);

total = sum(invalid_fieldvals);    
logging.warn('total = %d', total);










