my_list=[45,32,78,12,99]
n = len(my_list)

for i in range(n):      # loop for each item in my_list
    swapped = False 
    for j in range(0,n-i-1): # reduce the end value as things are sorted
        if my_list[j] > my_list[j+1]:   # '<' for decending order, array[j] comes first
            my_list[j], my_list[j+1] = my_list[j+1], my_list[j] # swapping both values
            swapped = True
    if not swapped:     # OR swapped == False
        # not False = True / not True = False
        break   # if nothing is swapped then it will break the loop

print("Sorted Array:", my_list) 