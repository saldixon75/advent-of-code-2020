import numpy;
import sys;
import re;


with open("input.txt") as f:
    lines = f.read().splitlines();

slots = lines[1].rsplit(',');
print("The slots are: ") + str(slots);
rules = {};
for i in range (len(slots)):
    if (slots[i] == 'x'):
        continue; # no rules for this slot.
    else:
        bus_id = int(slots[i]);
        rules[bus_id] = i;
print("The rules are: ") + str(rules);

for bus in sorted(rules.keys(),reverse=True):
    print("Bus " + str(bus) + " offset=" + str(rules[bus]));


def test_for_bus(timestamp, bus, offset):
    if ((timestamp + offset) % bus > 0):
        return False;
    print("PASSED " + " for bus= " + str(bus) + " timestamp=" + str(timestamp));        
    return True;

increment = 1;
timestamp = 0;
for bus in sorted(rules.keys(),reverse=True):
    while not test_for_bus(timestamp, bus, rules[bus]):
        timestamp += increment;
    #print("Woohoo! bus = " + str(bus) + " ts=" + str(timestamp) );    
    increment = increment * bus;
    print("Increment = " + str(increment));

print("Earliest good timestamp = " + str(timestamp));   



    












