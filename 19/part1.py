import numpy;
import sys;
import copy;
# import re;
import regex as re;

with open("input.txt") as f:
    input = f.read();
    
input_parts = input.split("\n\n");
rule_lines = input_parts[0].split("\n");    
messages = input_parts[1].split("\n");    

messages = filter(lambda x: not x == '', messages);

print('Parsed rule_lines = ' + str(rule_lines));
print('Parsed messages = ' + str(messages));

rules = {};

for rule_line in rule_lines:
    bits = rule_line.split(': ');
    rules[int(bits[0])] = bits[1];

print('Rule zero is..' + rules[0]);

#  build up a humungous regex, based on all the rules

def get_rule_regex(rule_number):
    regex = '';
    rule = rules[rule_number];
    print('rule='+rule);
    # either a stringy one, eg. "a"
    #  or a list of two other rules, eg. 69 12
    #  or two possible 2-rule combos, eg. 99 12 | 67 69
    # 
    # start with the easy one ("a" or "b")
    if ('"' in rule):
        print('here at the end of a chain...');
        regex = rule.replace('"','');
    elif ('|' in rule):
        # deal with the either/or scenario
        print('Dealing ith alternatives... ');
        alternative_sets = rule.split(' | ');
        print('alternatives sets = ... ' + str(alternative_sets));

        set1_regex = map(get_rule_regex,map(int,alternative_sets[0].split(' ')));
        set2_regex = map(get_rule_regex,map(int,alternative_sets[1].split(' ')));

        regex = '(' + ''.join(set1_regex) + '|' + ''.join(set2_regex)  + ')';
    else:
        # it's a list of one or more rules, one after the other
        subrules = list(map(int,rule.split(' '))); # In python3 map() retunrs a map object, unlike python2 which returns a list 
        # print('subrules are: ' + str(subrules));
        for i in range(len(subrules)):
            regex = regex + get_rule_regex(subrules[i]);
        # regex = get_rule_regex(subrules[0]) + get_rule_regex(subrules[1]); 
    return regex;    


reggie = '^' + get_rule_regex(0) + '$';


print('reggie = ' + reggie);

valid_messages = [];
for m in messages:
    if re.match(reggie, m):
        valid_messages.append(m);
        

print('grand total of valid messages =' + str(len(valid_messages)));        
print(valid_messages)

