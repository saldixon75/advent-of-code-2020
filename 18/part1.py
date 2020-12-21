import numpy;
import sys;
import copy;
import re;

with open("input.txt") as f:
    rows = f.read().splitlines();


#  no brackets expected in the expression parameter
def do_the_sum(expression):
    first_operand = re.match('\d+',expression).group();

    running_total = int(first_operand);
    pairs = re.findall(' [-*+] \d+',expression[len(first_operand):]);
    
    for pair in pairs:
        parts = re.match(' ([-*+]) (\d+)',pair).groups();
        operator = parts[0];
        digits = int(parts[1]);
        if ( operator == '+' ):
            running_total = running_total + digits;
        elif ( operator == '-' ):             
            running_total = running_total - digits;
        elif ( operator == '*' ):
            running_total = running_total * digits;
        else:
            print("EEK .. unknown operator: " + operator);
    print('expression evaluates to  = ' + str(running_total));
    return running_total;


def expand_innermost_brackets(string):
    inner_bracket_contents = re.findall('\(([^()]+?)\)', string);
    # print('number of finds = ' + str(len(inner_bracket_contents)) ); 
    expanded_string = string;
    for bracket_contents in inner_bracket_contents:
        evaluated = do_the_sum(bracket_contents);
        # now do a substitution 
        expanded_string = expanded_string.replace('(' + bracket_contents + ')',str(evaluated));
        print('es = ' + expanded_string);
    return expanded_string;    

grand_total = 0;

for row in rows:
    print('row = ' + row);
    while ('(' in row ):
        row = expand_innermost_brackets(row);        
    print('Full expanded string = ' + row);
    row_total = do_the_sum(row);
    print('row total = ' + str(row_total));
    grand_total += row_total;

print('Grand total = ' + str(grand_total));    

