import sys;
import re;

f = open("input.txt", "r")

contents = f.read();
# groups are separated by blank lines

groups = contents.split("\n\n");

running_total = 0;

for group in groups:
    stringy = '';
    answers = {''};
    people = group.splitlines();
    for person in people:
        #print("person = " + person);
        stringy = stringy + person;
        #print(list(person));
        for answer in list(person):
            answers.add(answer);
    answers.discard('');
    groupnum = len(answers);
    print("this group has " + str(groupnum) + "answers");
    running_total += groupnum;

print("TOTAL: " + str(running_total));

