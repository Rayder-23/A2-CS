# for this the array MUST be in sorted order

my_list = [11,12,22,25,34,64,90]
target_value = 64
found = False

low = 0
high = len(my_list) - 1

while low <= high:
    mid = (low + high) // 2

    if my_list[mid] == target_value:
        found = True
        break
    elif my_list[mid] < target_value:
        low = mid + 1
    else:
        high = mid - 1
    
if found:
    print("Item Found.")
else:
    print("Item not Found.")