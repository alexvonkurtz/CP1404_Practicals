LOWER = 33
UPPER = 127


character = input("Enter a character: ")
print("The ASCII code of '" + character + "' is",ord(character))
number = int(input("Enter a number between 33 and 127: "))

while number < LOWER or number > UPPER:
    print ("Invalid number")
    int(input("Enter a number between 33 and 127: "))
else:
    print ("The character of '" + str(number) + "' is",chr(number))

for ascii in range (33,127):
    print(ascii, '{:>10}'.format(chr(ascii)))


# at 100 the aligning shifts 1 space need to rectify