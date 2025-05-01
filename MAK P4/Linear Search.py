mylist = [23,34,1,43,2,60,80,58,90,123]
index = 0
found = False
item = int(input("Enter item to be searched: "))
# by default it takes it as string(str), we want int so we specify

while (found == False) and (index <= 9):
    if mylist[index]==item:
        found = True
    index = index + 1

if found == True:
    # print("Item Found.")
    print(f"{item} Found.") # f-stings, similar to template literals from JavaScript/TypeScript
else:
    # print("Item not Found")
    print(f"{item} not Found.")