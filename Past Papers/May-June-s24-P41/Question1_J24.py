# Part A)
DataStored = []
global NumberItems

# Part B)
def Initialise():
    global DataStored
    global NumberItems
    condition = True
    while condition:
        NumberItems = int(input("Enter Quantity of Items (1-20): "))
        if NumberItems > 1 and NumberItems <= 20:
            condition = False
        else:
            print("Invalid Quantity")
    
    for i in range(1,NumberItems+1):
        num = int(input("Enter Number:"))
        DataStored.append(num)
        # print(DataStored)
        
# Part C) i)
NumberItems = 0
Initialise()
print(DataStored)

# ii)
# Enter Quantity of Items (1-20): 30
# Invalid Quantity
# Enter Quantity of Items (1-20): 5
# Enter Number:3
# Enter Number:9
# Enter Number:4
# Enter Number:1
# Enter Number:2
# [3, 9, 4, 1, 2]

# Part D) i)
def BubbleSort(array):
    n = len(array)
    for i in range(n):
        swapped = False
        for j in range(0,n-i-1):
            if array[j] > array[j+1]:
                array[j+1],array[j] = array[j],array[j+1]
                swapped = True
        if not swapped:
            break
    
# ii)
BubbleSort(DataStored)
print(DataStored)

# iii) 
# Enter Quantity of Items (1-20): 5
# Enter Number:3
# Enter Number:9
# Enter Number:4
# Enter Number:1
# Enter Number:2
# [3, 9, 4, 1, 2]
# [1, 2, 3, 4, 9]

# Part E) i)
def BinarySearch(DataToFind):
    found = False
    low = 0
    high = len(DataStored) - 1
    while low <= high:
        mid = (low + high) // 2 
        if DataStored[mid] == DataToFind:
            found = True
            break
        elif DataStored[mid] > DataToFind:
            high = mid - 1
        else:
            low = mid + 1
    if found:
        return mid
    else:
        return -1
    
# ii)
Target = int(input("Enter Number to find: "))
print(BinarySearch(Target))

# iii)
# Enter Quantity of Items (1-20): 5
# Enter Number:1
# Enter Number:6
# Enter Number:2
# Enter Number:8
# Enter Number:10
# [1, 6, 2, 8, 10]
# [1, 2, 6, 8, 10]
# Enter Number to find: 2
# 1

# Enter Quantity of Items (1-20): 5
# Enter Number:1
# Enter Number:6
# Enter Number:2
# Enter Number:8
# Enter Number:10
# [1, 6, 2, 8, 10]
# [1, 2, 6, 8, 10]
# Enter Number to find: 7
# -1