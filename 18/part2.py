import numpy;
import sys;
import copy;
import re;

with open("input.txt") as f:
    rows = f.read().splitlines();


#  no brackets expected in the expression parameter
def do_the_sum(expression):
    #  need to give precedence to additions....
    first_operand = int(re.match('\d+',expression).group());

    parts = expression.split('*');
    bracketed_parts = map(lambda x: '(' + x + ')', parts);
    new_expression = '*'.join(bracketed_parts);
    total = eval(new_expression);
    return total; 



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
    # print('row = ' + row);
    while ('(' in row ):
        row = expand_innermost_brackets(row);        
    print('Full expanded string = ' + row);
    row_total = do_the_sum(row);
    print('row total = ' + str(row_total));
    grand_total += row_total;

print('Grand total = ' + str(grand_total));    

