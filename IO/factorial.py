def factorial(num):
	if num == 1:
		return 1
	else:
		return num * factorial(num-1)


num = input("Enter number: ")
fact = factorial(num)
print "\nFactorial of", num, "is:", fact
