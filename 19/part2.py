import numpy;
import sys;
import copy;
# import re;
import regex as re;
#  need python 3 for this, and the regex package (standard re has limit of 100 grouping expressiosn in a regex)

with open("input.txt") as f:
    input = f.read();
    
input_parts = input.split("\n\n");
rule_lines = input_parts[0].split("\n");    
messages = input_parts[1].split("\n");    

messages = list(filter(lambda x: not x == '', messages));
print('There are ' + str(len(messages)) + ' messages' );
print('There are ' + str(len(rule_lines)) + ' rules' );

rules = {};

for rule_line in rule_lines:
    bits = rule_line.split(': ');
    rules[int(bits[0])] = bits[1];

#  build up a humungous regex, based on all the rules

def get_rule_regex(rule_number):
    regex = '';
    rule = rules[rule_number];
    # print('rule='+rule);
    # either a stringy one, eg. "a"
    #  or a list of two other rules, eg. 69 12
    #  or two possible 2-rule combos, eg. 99 12 | 67 69
    # 
    # start with the easy one ("a" or "b") or any other literal regex
    if ('"' in rule):
        regex = rule.replace('"','');
    elif ('|' in rule):
        # deal with the either/or scenario
        alternative_sets = rule.split(' | ');

        set1_regex = map(get_rule_regex,map(int,alternative_sets[0].split(' ')));
        set2_regex = map(get_rule_regex,map(int,alternative_sets[1].split(' ')));

        regex = '(?:' + ''.join(set1_regex) + '|' + ''.join(set2_regex)  + ')';
    else:
        # it's a list of one or more rules, one after the other
        subrules = list(map(int,rule.split(' '))); # In python3 map() retunrs a map object, unlike python2 which returns a list 
        for i in range(len(subrules)):
            regex = regex + get_rule_regex(subrules[i]);
    return regex;    

def how_many(regex, string):
    count = 0;
    while( len(string) > 0 ) :
        print('string = ' + string + ', count = ' + str(count));
        if (re.match('(' + regex + ')?', string)):
            matchy = re.match('(' + regex + ')?', string).groups()[0];  #non-greedy. get as many as possible 
            string = string.replace(matchy,'',1);
            count += 1;
    return count;

print('Rule 0 is ' + str(rules[0]));

print('Original rule 8 = ' + rules[8]);
print('New rule 8 = 8: 42 | 42 8' );
print('Original rule 11 = ' + rules[11]);
print('New rule 8 = 11: 42 31 | 42 11 31' );


rule42 = get_rule_regex(42);
print('regex for rule 42 = \n' + rule42 + '\n');

rule31 = get_rule_regex(31);
print('regex for rule 31 = \n' + rule31+ '\n');

reggie = '^((?:' + rule42 + ')+)' + '((?:' + rule31 + ')+)$';


valid_messages = [];
for m in messages:
    if re.match(reggie, m):
        print('message = ' + m);
        # check what matched.  there needs to be more occurrences of the 41 group than the 31
        matched = re.search(reggie, m);

        #  how many fortTwo parts are there? 
        fortyTwomatch = how_many(rule42, matched.groups()[0]);
        thirtyOnematch = how_many(rule31, matched.groups()[1]);

        if (fortyTwomatch > thirtyOnematch):
            valid_messages.append(m);

print('grand total of valid messages =' + str(len(valid_messages)));        
