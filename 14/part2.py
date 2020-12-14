import numpy;
import sys;
import re;
import time;

start = time.time();

with open("input.txt") as f:
    lines = f.read().splitlines();

def unfloat(val, filler_string):
    splitty = val.split('X');
    number_of_chunks = len(splitty);
    if (number_of_chunks-1 != len(list(filler_string))):
        print("WARN!! val = " + val + " splitty = " + str(splitty) + " filler string = " + filler_string);
    
    rebuilt='';
    for i in range(len(filler_string)):
        rebuilt = rebuilt + str(splitty[i]) + list(str(filler_string))[i];
    
    rebuilt = rebuilt + str(splitty[number_of_chunks-1]);  
    return rebuilt;    

def get_mem_addresses(mem_slot_bin, mask):
    addresses = [];
    newval = '';
    valuebits = list(mem_slot_bin);
    maskbits = list(mask);
    for i in range(len(valuebits)):
        maskbit = maskbits[i];
        if (maskbit == '0'):
            newval = newval + valuebits[i]; # remains unchanged
        else: 
            newval = newval + maskbit; # overwritten with 1 or X
    # now we need to look for all the Xs and generate 2 ^ n entries in our addresses list.
    number_of_floaters = 0;
    if ('X' in mask):
        number_of_floaters = len(re.findall('X',mask));
    if (number_of_floaters == 0):
        return [newval];  #only one possible string

    number_of_permutations = 2 ** number_of_floaters;
    filler_string_format = '0' + str(number_of_floaters) + 'b';

    # print("NUMBER OF FLOATERS = "  + str(number_of_floaters) + " number_of_permutations = " + str(number_of_permutations));
    # print("FILLER STRING FORMAT = "  + filler_string_format + " MASK = " + mask);
    for combo_number in range(number_of_permutations):
        # eg. 0-3, 0-7, 0-15
        filler_string = format(combo_number, filler_string_format);

        addresses.append(unfloat(newval, filler_string));

    return addresses;    


mem = {};
mask_string = ''; 

for line in lines:
    if re.search('mask = ',line):
        mask_string = re.search('mask = (\w+)',line).group(1);
    else:
        match = re.search('mem\[(\d+)\] = (\d+)',line);
        mem_slot = int(match.group(1));
        dec_val = int(match.group(2));
        bit_val = format(dec_val, '036b');
        mem_slot_bin = format(mem_slot, '036b');
        mem_addresses = get_mem_addresses(mem_slot_bin, mask_string);

        for address in mem_addresses:
            mem[int(address,2)] = dec_val;
        

#print("Final memory state is: " + str(mem));   
total=0;
for key in mem.keys():
    total += mem[key];

end = time.time();
elapsed = end - start;

print("Grand total = " + str(total) + " (in " + str(elapsed) + " seconds)");













