import numpy;
import sys;
import re;


with open("input.txt") as f:
    lines = f.read().splitlines();


def apply_mask(value, mask):
    newval = '';
    valuebits = list(value);
    maskbits = list(mask);
    # print("In apply_mask. value=" + value + " mask=" + mask);
    # print("valuebits = " + str(valuebits) + "maskbits = " + str(maskbits));
    for i in range(len(valuebits)):
        maskbit = maskbits[i];
        if (maskbit == 'X'):
            newval = newval + valuebits[i];
        else:
            newval = newval + maskbit;
    return newval;


mem = {};
mask_string = ''; 

for line in lines:
    if re.search('mask = ',line):
        mask_string = re.search('mask = (\w+)',line).group(1);
        print("New mask! " + mask_string + " len=" + str(len(mask_string)));
    else:
        match = re.search('mem\[(\d+)\] = (\d+)',line);
        mem_slot = int(match.group(1));
        dec_val = int(match.group(2));
        print("Instruction is write " + str(dec_val) + " to memslot " + str(mem_slot));
        bit_val = format(dec_val, '036b');
        # print("bit val = " + str(bit_val));
        masked_value = apply_mask(bit_val, mask_string);
        print("New val = " + masked_value);
        mem[mem_slot] = int(masked_value,2);

print("Final memory state is: " + str(mem));   
total=0;
for key in mem.keys():
    total += mem[key];

print("Grand total = " + str(total));











