# Definition: A recursive routine is a function or algorithm that calls itself during its 
# excution, either directly or indirectly, to solve a smaller instance of the same problem, 
# for e.g Factorial Problem

def factorial(n):
    if n == 0 or n == 1: # FIX: 'n == 1', otherwise python assumes that alone 1 as true
        return 1    # base case: factorial of 0 or 1 is 1
    else:
        return n * factorial(n - 1)  # recursive step: n * (n-1)!
        # the function itself is repeated to solve the problem
    
num = 5
result = factorial(num)
print(f"The factorial of '{num}' is: '{result}'.")  # 5! = 120