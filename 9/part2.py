import sys;
import re;

with open("input.txt") as f:
    lines = f.read().splitlines();

rogue_line =  15;
rogue_number =  127;
rogue_line =  560;
rogue_number =  90433990;

def is_valid(clump):
    running_total = 0;
    lines_added = 0;
    # start from the highest, and work down. Quickest way to rule out the clump by breaching the target number
    for line_to_add in range(len(clump),1,-1):
        running_total += clump[line_to_add-1];
        lines_added += 1;
        #print("lines_added " + str(lines_added) + ", running_total = " + str(running_total));
        if (running_total > rogue_number):       
            return False;
        if ( (running_total == rogue_number) and lines_added > 2):
            print("WE HAVE A WINNER!!! lines_added = " + str(lines_added) + " , from " + str(clump[-1]) + " downwards");
            constiguous_section = clump[len(clump)-lines_added:len(clump)];
            sorted_section = sorted(constiguous_section);
            smallest_number = sorted_section[0];
            largest_number = sorted_section[-1];
            print("The contiguous section is " + str(clump[len(clump)-lines_added:len(clump)]));
            print("SUM = " + str(smallest_number  + largest_number));
            return True;
           
    return False;

for i in range(rogue_line-1,1,-1):
    #print("starting countdown from line " + str(i) + " number=" + lines[i-1]);

    candidate_clump = map(int, lines[0:i-1]);
    #print(candidate_clump);

    if ( is_valid(candidate_clump)):
       print("VALID CLUMP FOUND! i=" + str(i));
       break;   
