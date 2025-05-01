# for this the array MUST be in sorted order

# first we use the lowerbound and upperbound to get the mid point
# then we check the MP for the item, 
# after that we update the lb to be on the right of the MP (<)
# or we update the ub to be on the left of the MP, depends on where the item using size (>)
# do the same process again until we find the item

mylist = [23,33,45,55,60,70,88,200,500]
found = False
lb = 0
ub = len(mylist)-1    # (length of array) - 1
item = int(input("Enter item to be searched: "))

while (found == False) and (lb <= ub):
    midpoint = (lb+ub)//2   # needs to be "//" for division with int

    if mylist[midpoint] == item:
        found = True
    elif mylist[midpoint] > item:   # needs to be > here
        ub = midpoint - 1
    else:
        lb = midpoint + 1
    
if found == True:
    print(f"{item} Found.")
else:
    print(f"{item} not Found.")
