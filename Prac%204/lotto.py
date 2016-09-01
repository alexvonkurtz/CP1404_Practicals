from random import randint

NUMBER_OF_VALUES = 6

def main():
    set_number_of_lines = int(input("How many lines would you like to generate?: ")) # Set number of lines to generate

    random_numbers_unique(set_number_of_lines)


def random_numbers_unique(set_number_of_lines):
    for i in range(set_number_of_lines):
        line_numbers = [] # Open list to be appended of random generated numbers
        for j in range(NUMBER_OF_VALUES): #

            # Get a set of unique generated numbers
            chosen_number = randint(1,45)
            while chosen_number in line_numbers:
                chosen_number = randint(1,45)
            # print("{}".format(chosen_number))

            line_numbers.append(chosen_number)
        print(line_numbers)


main()