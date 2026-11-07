try:
	age = int(input("How old are you? "))
	if age < 0:
		print("Please enter a valid age.")
	elif age >= 18:
		print("You can drive.")
	else:
		print("You cannot drive yet.")
except ValueError:
	print("Please enter your age as a whole number.")
