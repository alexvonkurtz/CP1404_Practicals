numbers = [3, 1, 4, 1, 5, 9, 2]


print(numbers[0]) #Should print 3, as 3 is in the zero spot and 1 is first spot and 4 is second
#Tested above and correct

print(numbers[-1]) #Will it print 9,1,1,3 as decreasing from final?
#Tested above and returned 2 so therefore it started at 0 spot (being 3) and went back 1 to last spot being number 2

print(numbers[3]) #Will it print 1 as the number 1 is in the third postition?
#Tested above and correct

print(numbers[:-1]) #Since ':' indicates the beggining i am assuming it will print 2,9,5,1,4,1,3
#Printed [3,1,4,1,5,9] therefore printed all but number in the -1 spot therefore being the number 2

print(numbers[3:4]) #This is indicating to me numbers 3 to 4 which as 1 and 5
#Tested above and it only printed the number 1 therefore the fourth place is no included as a final place

print(5 in numbers) #Expect this to be true as the number 5 is included within the list
#Tested and the above proves to be True

print(7 in numbers) #Expect this to be false as the number 7 is not included within the list
#Tested and the above is False

print("3" in numbers) #Expect this to be false as "3" is indicating it is a string?
#Tested the above and the result is False, did another test by removing the double quotation marks and returned True

print(numbers + [6, 5, 3]) #This is indicating to me that all numbers in the list PLUS the number 6,5, and 3.
#Therefore including these numbers to the list to have [3,1,4,1,5,9,2,6,5,3]
#Tested the above and my explanation proved to be correct
