x = int(input("Enter Your first number:  "))
y = int(input("Enter Your secoind number:  "))

print("\nThis is a menu based program. Therefore enter the Number of menu to select which operation you would prefer:  \n")
print("1 -> Addition.")
print("2 -> Subtraction.")
print("3 -> Division.")
print("4 -> Multiplication.\n")

z = int(input("Please enter your option here:  "))

if z == 1:
	n = x+y
	print("\nThe sum of your number is: ",n)
	print("\nThank you")

elif z ==2:
	e = x-y
	r = y-x
	print("\nFor the order (x-y) the difference is: ",e," and for the order (y-x) the difference is: ",r)
	print("\nThank you")

elif z ==3:
	q = x/y
	w = y/x
	print("\nFor the order (x/y) the difference is: ",q," and for the order (y/x) the difference is: ",w)
	print("\nThank you")

elif z == 4:
	o = x*y
	print("\nThe sum of your number is: ",o)
	print("\nThank you")

else:
	print("\nCheck the menu and try again.")
	print("\nThank you")