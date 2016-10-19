# A soccer team is looking for girls from ages 10 to 12 to play on their team.
# The program will ask the user's age and whether the user is male or female (m/f)
# The messae will display whether the person is eligible to play on the team.


 age = int(input("Enter your age: "))
gender = input("Enter your gender, m/f : ")

if age>10 and age<12:
	if gender == 'f':
		print("you are eligible to join the team")
	else:
		print("you are not eligible to join the team ")
else:
	print("you are not eligible to join the team because of your age")