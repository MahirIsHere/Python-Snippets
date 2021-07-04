num = int(raw_input("\nEnter num: "))

rev = 0
while(num != 0):
	rev = rev*10
	rev = rev+num % 10
	num = num/10

print "Reverse number: ", rev
