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
    name = match.group(1);
    valid_range_1 = map(int, match.group(2).split('-'));
    valid_range_2 = map(int, match.group(3).split('-'));
    # logging.debug(valid_range_1);
    return [name, valid_range_1, valid_range_2];

def passes_rule(rule, values):
    print('in passes_rule.  rule = ' + str(rule) +  ' values = ' + str(values));
    # print('in passes_rule.  values = ' + str(values) );
    for value in values:
        if ( not ( value >= rule[1][0] and value <= rule[1][1] or (value >= rule[2][0] and value <= rule[2][1]) )):
            # print(str(value) + ' failed: ' + str(rule[1][0]) + ', ' + str(rule[1][1]) + ', '+ str(rule[2][0]) + ', ' + str(rule[2][1]));
            print('FAIL! for val=' + str(value)) + ' rule[1][0]=' + str(rule[1][0]);
            return False;
    print('PASS!');
    return True;

def is_valid(ticket):
    #  ticket is simply a list of integers
    for fieldvalue in ticket:
        # does every number in the ticket match satisfy at least one rule?
        passes = False;
        for rule in fieldrules:
            # found a rule that passes, so this field  value is fine
            if (passes_rule(rule, [fieldvalue])):
                passes = True;
                break;
        if (not passes):
            return False;
    return True;

fieldrules = map(parse_rule,fileparts[0].split("\n"));
myticket = parse_ticket(fileparts[1].split("\n")[1]);

nearbytickets = fileparts[2].split("\n");
nearbytickets.remove('');
nearbytickets.remove('nearby tickets:');

# weed out the invlaid tickets
allnearbytickets = map(parse_ticket, nearbytickets);
nearbytickets = filter(is_valid,allnearbytickets);   

print('allnearbytickets: ' + str(len(allnearbytickets)) + ' valid ones: ' + str(len(nearbytickets)) );     
# END weed out the invlaid tickets

# sys.exit();

# print("all rules = " + str(fieldrules));
logging.info('my ticket = %s', myticket);


column_candidates = {};
rule_columns = {};


for i in range(len(fieldrules)):
    print("Inspecting column " + str(i+1));
    #  get all the nearby ticket values for this column
    column_values = [];
    for ticket in nearbytickets:
        column_values.append(ticket[i]);  # inefficient.  could use a set instead
    # now run each fieldrule against this set of values to see which rules pass...
    print('column values = ' + str(column_values));
    passing_rules = [];
    for fieldrule in fieldrules:
        passing = passes_rule(fieldrule, column_values);
        if (passing):
            passing_rules.append(fieldrule[0]);
    column_candidates[i] = passing_rules;
    print('COLUMN ' + str(i) + ' HAS ' + str(len(passing_rules)) + ' CANDIDATE RULES');
    if len(passing_rules) == 1:
        rule_columns[passing_rules[0]] = i;

print("First pass Column candidates = " + str(column_candidates)); 
print("First pass known rule columns =  = " + str(rule_columns)); 


while len(column_candidates.keys()) > 0:
    for column in column_candidates.keys():
        # print('Looking aat column ' + str(column) );
        if (len(column_candidates[column]) == 0):
            column_candidates.pop(column);
            continue;
        elif (len(column_candidates[column]) == 1):
            # print('yes! length is 1 for column=' + str(column));
            rule_columns[column_candidates[column][0]] = column;
            column_candidates.pop(column);
            # print('column_candidates is now ...' + str(column_candidates));
            continue;      
        # weed out the rules that have already been taken...
        else:
            # print('length is >1 for column=' + str(column));
            for candidate in column_candidates[column]:
                # print('checking candidate ' + str(candidate) + ' looking in rule_columns: ' + str(rule_columns));
                if (candidate in rule_columns):
                    # print('aha! this one has already been nailed down..' + candidate );
                    column_candidates[column].remove(candidate);
    # print("column_candidates = " + str(column_candidates));



print("Column candidates = " + str(column_candidates)); 
print("Know rule columns =  = " + str(rule_columns));  

my_departure_fields = [];
for rulename in rule_columns.keys():
    if re.search('departure', rulename):
        my_departure_fields.append(myticket[rule_columns[rulename]]);

print('my_departure_fields = ' + str(my_departure_fields));

total = numpy.prod(my_departure_fields);
print('total = ' + str(total));
# column_definites = {};
# for column in column_candidates.keys:
#     print('column')


# Column candidates = {0: ['row'], 1: ['class', 'row'], 2: ['class', 'row', 'seat']}
# Know rule columns =  = {0: 'row'}















