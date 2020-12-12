import sys;
import re;

with open("input.txt") as f:
    lines = f.read().splitlines();


buffer_size = 25;

def is_valid(num, buffer):
    for a in range(buffer_size): 
        for b in range(a+1, buffer_size): 
            #print("a = " + str(buffer[a]) + " b=" + str(buffer[b]));
            if ( (buffer[a] + buffer[b] == num) and (buffer[a] != buffer[b]) ):
                print("hooray");
                return True;
    return False;


for i in range(buffer_size+1,len(lines)):
    num = int(lines[i-1]);
    #print("i = " + str(i) + " number = " + str(num));

    buffer = map(int, lines[i-buffer_size-1:i-1]);
    #print(buffer);

    if (not is_valid(num, buffer)):
       print("ROGUE ENTRY FOUND!! i=" + str(i) + " number=" + str(num));
       break;   
