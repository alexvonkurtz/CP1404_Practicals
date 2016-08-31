#ask user for name
# error checking to make sure username not blank
# print every second letter in name
# use for loop, range and length of the name

def main():
    userName = get_name()
    method_name(userName)


def method_name(userName):
    increment = int(input("Enter increment number: "))
    print(userName[0::increment])


def get_name():
    userName = input("Please enter your name: ")
    while userName == "":
        print("You did not enter anything")
        userName = input("Please enter your name: ")
    return userName


main()