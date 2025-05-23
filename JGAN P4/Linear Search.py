my_list = [3,5,2,8,9,1]
target = 9
Found = False

for i in range(len(my_list)):
    if my_list[i] == target:
        Found = True
        break

# OR
# loop for each element inside of checking each index
for i in my_list:
    if i == target:
        Found = True
        break

if Found:
    print("Target found.")
else:
    print("Target not found.")