import sys;
import numpy;

with open("input.txt") as f:
    lines = f.read().splitlines();

adaptors = map(int,lines);
adaptors.append(0);
adaptors.sort();

print(adaptors);
print("Number of adaptors  =  " + str(len(adaptors)));

jumps = [];

# build up a list of 'jumps', ie. the diff in joltage between adjacent adaptors
current_joltage = 0;

for adaptor in adaptors:
    diff = adaptor - current_joltage;
    #print("previous = " + str(current_joltage) + " current=" + str(adaptor) );
    if (diff > 0):
        jumps.append(diff);
    current_joltage = adaptor;
    
print("Number of jumps = " + str(len(jumps)));
#print(jumps);

# Now split by the '3' jumps ... these demarcate discreet groups of jumps which can have >! permutation
clumps = list(filter( lambda clumpstring: len(clumpstring) > 0 , ''.join(str(x) for x in jumps).split('3') ));

print(clumps); 

clump_combos = {
    1: 1,
    2: 2,
    3: 4,
    4: 7
};

clump_combinations = [];

for clump in clumps:
    #print("CLUMPSIZE="+ str(len(clump)) + " clump = " + str(clump) );
    number_of_permutations = clump_combos[len(clump)];
    #print("number_of_permutations = " + str(number_of_permutations));
    clump_combinations.append(number_of_permutations);
    
total_combos = numpy.prod(clump_combinations);
print("grand total is: " + str(total_combos));


