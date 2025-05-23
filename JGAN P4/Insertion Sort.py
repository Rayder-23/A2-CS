my_list = [3,5,2,8,9,1]

for i in range(1,len(my_list)):
    key = my_list[i]    # starts at 2nd position of array and saves it
    j = i - 1   # j is always one position behind i

    # j can't be lesser than 0, that would be out of the array
    while (j >= 0) and (my_list[j] > key):  # 'key <' for deccending order, array[j] comes first
        my_list[j+1] = my_list[j]
        # [i] here doesn't work, needs to be j+1
        j -= 1

    my_list[j+1] = key

print("Sorted Array:", my_list)