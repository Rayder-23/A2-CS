# for this the array MUST be in sorted order, accending or deccending

my_list = [11,12,22,25,34,64,90]
target_value = 64
found = False

low = 0 # lowerbound
high = len(my_list) - 1 # upperbound

while low <= high:
    mid = (low + high) // 2 # // gives int, no floating point

    if my_list[mid] == target_value:
        found = True
        break
    elif my_list[mid] < target_value:
        low = mid + 1   # move lb up, '-1' since we don't need to include mid
    else:
        high = mid - 1  # move hb down
    
if found:
    print("Item Found.")
else:
    print("Item not Found.")