"""
Python file to calculate and print all teh first n fibonacci numbers
using memoization

Time Complexity is O(n) instead of O(1.6 ^ N) if we had not used memoization
"""

def calculatefib(n):
	"""
	Function to calculate the nth fibonacci number
	"""
	
	# Create a list of length n + 1 initilaized with all zeros
	memo = [0] * (n+1)
	
	# Call the fibonacci function
	for i in range(1,n+1):
		# Since the count starts from 1
		# using the range(1, n+1) while printing
		print("Fib ", i, " = ", fib(i-1, memo))

	

	
def fib(n, memo):
	"""
	This function does teh actual work
	This function is called recursively
	"""
	
	if n <= 0:
		return 0
	
	elif n == 1:
		return 1
	
	# If already memoized then return that value
	elif memo[n] > 0:
		return memo[n]
	
	# Else memoize the values
	memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
	
	return memo[n]
	

calculatefib(67)