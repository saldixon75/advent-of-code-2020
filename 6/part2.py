import sys;
import re;

f = open("input.txt", "r")

contents = f.read();
# groups are separated by blank lines

groups = contents.split("\n\n");

running_total = 0;

for group in groups:
    firstperson = re.match('(\w+)',group).group(0);
    #print("first person = " + firstperson);
    answers = set(list(firstperson));
    people = group.splitlines();
    for person in people:
        #print(list(person));
        answers =  set(list(person)).intersection(answers);
    answers.discard('');
    groupnum = len(answers);
    print("this group has " + str(groupnum) + " common answers");
    running_total += groupnum;

print("TOTAL: " + str(running_total));

