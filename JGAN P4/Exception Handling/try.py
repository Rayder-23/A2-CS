try:
    number = int(input("Enter a number: "))
    result = 10 / number 
    print(f"The result is: {result}.")

except ZeroDivisionError:   # if this error occurs, the above code is neglected and this block plays
    print("Error: Cannot Divide by Zero.")

except Exception as e:  # if any other error occurs
    print(f"Error: {e}")

finally:    # the finally block always runs
    print("\nThis code will always run.")