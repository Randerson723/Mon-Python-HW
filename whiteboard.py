# Write a function to print all numbers 1 to n, but there are some constraints
# If the number is divisible by 3, print 'Fizz' instead of the number
# If the number is divisible 5, print 'Buzz' instead of the number
# If the number is divisible by both 3 and 5, print 'FizzBuzz' instead of the number
# Otherwise, simply print the number
def fizzBuzz(n):
    
    if n % 3 == 0 and n % 5 == 0:
        return "Fizzbuzz"
    if n % 3 == 0:
        return "Fizz"
    if n % 5 == 0:
        return "Buzz"
    else:
        return n


print(fizzBuzz(9)) # Should return 'Fizz'
print(fizzBuzz(10)) # Should return 'Buzz'
print(fizzBuzz(15)) # Should return 'FizzBuzz'
print(fizzBuzz(4)) # Should return 4

# Python 3.x code to demonstrate star pattern

# Function to demonstrate printing pattern triangle
def triangle(n):
	
	# number of spaces
	k = n - 1

	# outer loop to handle number of rows
	for i in range(0, n):
	
		# inner loop to handle number spaces
		# values changing acc. to requirement
		for j in range(0, k):
			print(end=" ")
	
		# decrementing k after each loop
		k = k - 1
	
		# inner loop to handle number of columns
		# values changing acc. to outer loop
		for j in range(0, i+1):
		
			# printing stars
			print("* ", end="")
	
		# ending line after each row
		print("\r")

# Driver Code
n = 5
triangle(n)
