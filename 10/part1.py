import sys;
import re;

with open("input.txt") as f:
    lines = f.read().splitlines();


#adaptors = map(int,lines).sort());
adaptors = map(int,lines);
#adaptors.append(0);
adaptors.sort();

print(adaptors);

jumps = {
    1: 0,
    2: 0,
    3: 0    
};

current_joltage = 0;
for adaptor in adaptors:
    diff = adaptor - current_joltage;
    print("previous = " + str(current_joltage) + " current=" + str(adaptor) );
    jumps[diff] = jumps[diff] + 1;
    current_joltage = adaptor;
    

jumps[3] = jumps[3] + 1;

print (jumps);
result = jumps[1] * jumps[3];
print("Result = " + str(result));
