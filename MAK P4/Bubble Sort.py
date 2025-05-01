# declare array
mylist = [23,1,20,15,100,8]
#unsorted
print(mylist)

lb = 0 # lowerbound
ub = 5 # upperbound
swap = True     # don't try to declare in one line

while (swap == True) and (ub >= 0):
    swap =  False   # boolean is used to make the code efficient
    
    for index in range(ub):     #index starts at 0
        if mylist[index] > mylist[index+1]:   # change sign to < to make it into decending order 
            #swap
            temp = mylist[index]
            mylist[index] = mylist[index+1]
            mylist[index+1] = temp
            swap = True     # if it doesn't swap, means the array is sorted and it stops in one for-loop
    #outside for-loop
    ub = ub-1

#sorted
print(mylist)
