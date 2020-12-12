import sys;
import re;

with open("input.txt") as f:
    rules = f.read().splitlines();

directly_containing = {};

for rule in rules:
    print("\n" + rule);
    nowtinside  = re.match('(\w+ \w+) bags contain no other bags',rule);
    if (nowtinside):
        bag = nowtinside.group(1).replace(' ','-');
        print("bag with nowt in = " + bag);
        continue;
    print("Checking what is contained...");

    containingbag = re.match('(\w+ \w+) bags contain',rule).group(1);
    print("contaningbag - " + str(containingbag));
    
    insidebags = re.findall('(\d+ \w+ \w+ bags?[,.]\s?)',rule); 
    print("insidebags are: "); 
   
     
    for innerbag in insidebags:
        deets = re.match('(\d+) (\w+ \w+)',innerbag);
        innerbagname = deets.group(2);        
        innerbagnumber =  deets.group(1);        
        print(innerbagname);

        direct_containers = directly_containing.get(innerbagname);
        print("existing direct_containers = " + str(direct_containers)); 
        if (not direct_containers):
            direct_containers =  set([containingbag]);
        else:
            direct_containers.add(containingbag);
        print("updated direct_containers = " + str(direct_containers)); 
        directly_containing[innerbagname] = direct_containers;


bag_of_interest = 'shiny gold';
print(bag_of_interest + " HAS the following possibilities for direct containment: " + str(directly_containing.get(bag_of_interest)));

# Need to find shiny gold's directly_contaning bags (easy), but also all *their* containing bags, and so on.
#  but avoid an infinite loop! Need some recursion with a breakout condition.

def add_containing_bags(bagname, existing_set):
    # iIf they don't already exist in the existing set, get the direct containers of bagname.      
    direct_containers = directly_containing.get(bagname);
    if (not direct_containers):
        print("nothing directly contains " + bagname + "... returning");
        return existing_set;
    new_bags = direct_containers.difference(existing_set);
    updated_set = existing_set.union(new_bags);
    for bag in new_bags: 
        updated_set = add_containing_bags(bag, updated_set);   
    return updated_set;


all_containing_bags = add_containing_bags(bag_of_interest, set([])); 

print(bag_of_interest + " has " + str(len(all_containing_bags)) + " possibilities for ANY containment. They are:  " + str(all_containing_bags));
