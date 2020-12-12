f = open("input.txt", "r")

orig_numbers = f.readlines();
numbers = map(int, map(str.strip, orig_numbers));

# Iterate the list using for loop
for number1 in numbers:
    for number2 in numbers:
        if (number1 + number2 == 2020):
            print("Found 'em..." + str(number1) + ", " + str(number2) + ", multiplied they are" + str(number1*number2));
            exit;
    
