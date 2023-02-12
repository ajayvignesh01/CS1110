number_1_10 = input('Pick a number between 1 and 10: ')
number_2_5_50 = ((int(number_1_10) * 2) + 5) * 50
birthday_this_year = input("If you've already had a birthday this year, enter 1772. Otherwise, enter 1771: ")
number_2_5_50_177x = number_2_5_50 + int(birthday_this_year)
birth_year = input("Enter the year that you were born: ")
number_2_5_50_177x_200x = number_2_5_50_177x - int(birth_year)
age = int(number_2_5_50_177x_200x) % 100
print('The magic number is "' + str(number_2_5_50_177x_200x) + '". That means you are ' + str(age) + '!')