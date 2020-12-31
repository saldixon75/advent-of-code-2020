import numpy;
import sys;
import copy;
import re;


with open("input.txt") as f:
    lines = f.readlines();
    
print('There are ' + str(len(lines)) + ' lines' );

known_ingredients_dict = {};  # ingredients which have an identified allergen
known_allergens_dict = {}; # for each allergen, as set of candidate ingredients

allergen_candidates = {}; # for each allergen, as list of candidate ingredients

all_ingredients = {};


for line in lines:
    matched = re.match('([\w\s]+) \(contains ([\w+,\s]+)\)$', line ).groups();
    ingredients = matched[0].split();
    allergens = matched[1].split(', '); 
    print('line = ' + line + ' ingredients = ' + str(ingredients) + ' allergens = ' + str(allergens));
    
    for ingredient in ingredients:
        if ingredient in all_ingredients:
            all_ingredients[ingredient] = all_ingredients[ingredient]+1;
        else:
            all_ingredients[ingredient] = 1;

    for allergen in allergens:
        if allergen in allergen_candidates:
            candidate_ingredients = allergen_candidates[allergen];
            candidate_ingredients.intersection_update(set(ingredients));
        else:
            allergen_candidates[allergen] = set(ingredients);

print('allergen_candidates  = ' + str(allergen_candidates));             
number_of_allergens = len(allergen_candidates.keys());
print('number of allergens = ' + str(number_of_allergens));

#  now build up a list of definites

def prune_allergen_candidates(allergen_candidates):
    # for allergen in allergen_candidates:
    global known_ingredients;
    revised_allergen_candidates = {};
    for allergen in allergen_candidates:
        if len(allergen_candidates[allergen]) == 1:
            ingredient = allergen_candidates[allergen].pop();
            #  remove it altogethre from alleegen_candidates dict
            known_ingredients_dict[ingredient] = allergen;
            known_allergens_dict[allergen] = ingredient;
        else:
            revised_allergen_candidates[allergen] = allergen_candidates[allergen];

        # # now remove known ingredients from other allergen candidates....
        if allergen in revised_allergen_candidates:
            print('revised_allergen_candidates[allergen] = ' + str(revised_allergen_candidates[allergen]));
            revised_allergen_candidates[allergen].difference_update(set(known_ingredients_dict.keys()));    

    #
    return revised_allergen_candidates;

while (len(allergen_candidates) > 0):
    allergen_candidates = prune_allergen_candidates(allergen_candidates);    

print(allergen_candidates);
print('all ingredients = ' + str(all_ingredients));
print('known_ingredients with allergens' + str(known_ingredients_dict));
print('known_allergens' + str(known_allergens_dict));

nonallergenic_ingredients = set(all_ingredients.keys());
nonallergenic_ingredients.difference_update(set(known_ingredients_dict.keys()));
print('nonallergenic_ingredients = ' + str(nonallergenic_ingredients));

running_total = 0;
for safe_ingredient in nonallergenic_ingredients:
    running_total += all_ingredients[safe_ingredient];

print('total = ' + str(running_total));     

#  part 2 get the canonical list

aphabetical_allergens = sorted(known_allergens_dict.keys());
print('aphabetical_allergens=' + str(aphabetical_allergens));
dangerous_ingredients = [];
for allergen in aphabetical_allergens:
    dangerous_ingredients.append(known_allergens_dict[allergen]);

print(','.join(dangerous_ingredients));    