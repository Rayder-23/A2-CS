mylist = [23,10,18,200,50,40]
print(mylist)

# lb is usually the next num, ub can be the length of the list
for index in range(1,6):    # (lb, ub)
    iteminsert = mylist[index]  # saves the number
    currentitem = index - 1     # selects the number before iteminsert
    
    while (mylist[currentitem] > iteminsert) and (currentitem > -1):    # change sign to < for decending
        mylist[currentitem +1] = mylist[currentitem]    # copies the value before iteminsert to iteminsert
        currentitem = currentitem -1    # goes 2 position before iteminsert to check that via while-loop
    mylist[currentitem +1] = iteminsert # puts the original number in the correct place
    # loops until sorted

print(mylist)