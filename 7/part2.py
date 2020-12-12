import sys;
import re;

with open("input.txt") as f:
    rules = f.read().splitlines();

directly_contains = {};

for rule in rules:
    print("\n" + rule);
    nowtinside  = re.match('(\w+ \w+) bags contain no other bags',rule);
    if (nowtinside):
        bag = nowtinside.group(1);
        print("bag with nowt in = " + str(bag));
        continue;

    containingbag = re.match('(\w+ \w+) bags contain',rule).group(1);
    print("contaningbag - " + str(containingbag));
    
    insidebags = re.findall('(\d+ \w+ \w+ bags?[,.]\s?)',rule); 
    print("insidebags are: "); 
    contains = {};
    for innerbag in insidebags:
        deets = re.match('(\d+) (\w+ \w+)',innerbag);
        innerbagname = deets.group(2);        
        innerbagnumber =  deets.group(1);        
        print(innerbagname);
        contains[innerbagname] = innerbagnumber;
    directly_contains[containingbag] = contains;


bag_of_interest = 'shiny gold';
print(bag_of_interest + " directly contains the following : " + str(directly_contains.get(bag_of_interest)));

# Need to find all the bags that shiny gold directly contans (easy), but also all the ones they contains, and so on...
#  but avoid an infinite loop! Need some recursion with a breakout condition.


def get_number_of_contained_bags(bagname):
    print("Looking in " + bagname);
    directly_contained = directly_contains.get(bagname);
    if (not directly_contained):
        print("contains NOWT: " + bagname + "... returning");
        return;
    for bagtype in directly_contained: 
        num = int(directly_contained[bagtype]);
        print(str(bagtype) + ": " + str(num));
        global running_total;
        running_total += num; # first add the bags themslevs 
        for i in range(1, num+1):        
            get_number_of_contained_bags(bagtype);  

print("HERE WE GO");


running_total = 0;
all_contained_bags = get_number_of_contained_bags(bag_of_interest); 

print(bag_of_interest + " contains " + str(running_total) + " bags");
