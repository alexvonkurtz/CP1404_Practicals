def main ():
    LOWER = 33
    UPPER = 127
    character = input("Enter a character: ")
    print("The ASCII code of '" + character + "' is",ord(character))
    number = get_number(LOWER, UPPER)
    print("The character of '" + str(number) + "' is", chr(number))
    for ascii in range(10, 50):
        print(ascii, '{:>10}'.format(chr(ascii)))

def get_number(LOWER,UPPER):
    while True:
        try:
            number = int(input("Enter a number between 10 and 50: "))
        except ValueError:
            print ("Please enter a valid number!")
            continue
        if number < LOWER or number > UPPER:
            print ("Please enter a valid number!")
        else:
            return number
main()