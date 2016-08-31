"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    incomes = []
    inputted_number_of_months = int(input("How many months? "))

    for month in range(1, inputted_number_of_months + 1):
        income = float(input("Enter income for month " + str(month) + ": ")) #TODO change income to str.format
        incomes.append(income)

    compiled_month_income_report(incomes, inputted_number_of_months)


def compiled_month_income_report(incomes, inputted_number_of_months):
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, inputted_number_of_months + 1):
        income = incomes[month - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))


main()