import sys;
import re;

f = open("input.txt", "r");
lines = f.readlines();
lines = map(str.strip, lines);


def get_row(boarding_pass):
    code  = re.match("(\w{7})",boarding_pass).group(1);
    binary = int(code.replace('F','0').replace('B','1'),2);
    #print("row number =  " + str(binary));    
    return binary;


def get_column(boarding_pass):
    code  = re.match("(\w{7})(\w{3})",boarding_pass).group(2);
    binary = int(code.replace('L','0').replace('R','1'),2);
    #print("column number =  " + str(binary));    
    return binary;

seats = {0};

for bpass in lines:
    row = get_row(bpass);
    column = get_column(bpass);
    #print("Seat is row " + str(row) + " column " + str(column));
    seat_id = row * 8 + column;
    #print("Seat id = " + str(seat_id));
    print(seat_id);
    seats.add(seat_id);

i=12;
while i < 871:
    if (not i in seats):
        print("Your seat number is: " + str(i)); 
    i +=1;

