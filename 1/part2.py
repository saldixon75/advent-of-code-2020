import sys;

f = open("input.txt", "r")

orig_numbers = f.readlines();
numbers = map(int, map(str.strip, orig_numbers));

# Iterate the list using for loop
for number1 in numbers:
    for number2 in numbers:
        for number3 in numbers:
            if (number1 + number2 + number3 == 2020):
                print("Found 'em..." + str(number1) + ", " + str(number2) + ", " + str(number3) + ", multiplied they are " + str(number1*number2*number3));
                sys.exit();
    
