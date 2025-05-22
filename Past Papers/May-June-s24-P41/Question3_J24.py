# Part A)
global QueueData
global QueueHead
global QueueTail
QueueData = [""]*20
QueueHead = -1
QueueTail = -1

# Part B)
def Enqueue(data):  # add at tail
    global QueueHead, QueueTail
    if QueueTail == 19: # Queue is full as 19 is last valid postion, Array[0-19]
        return False
    elif QueueHead == -1:  # # Set head to first position if queue was empty
        QueueHead = 0
    QueueTail += 1  # Move tail forward
    QueueData[QueueTail] = data # Insert data at the tail position
    return True

# Part C)
def Dequeue():  # remove at head
    global QueueData
    global QueueHead
    global QueueTail
    if QueueHead < 0 or QueueHead > 20 or QueueHead > QueueTail:
        return False    # Queue is empty or invalid
        # QueueHead < 0: Queue hasn't started yet
        # QueueHead > 20: Invalid index, 19 is last index (out of range)
        # QueueHead > QueueTail: All items have been dequeued — so the queue is logically empty
    else:
        item = QueueData[QueueHead] # Remove head
        QueueHead = QueueHead + 1   # Move head forward
    if QueueHead > QueueTail:   # reset queue
            QueueHead = -1
            QueueTail = -1
    return item    

# Part D) i)
def StoreItems():
    invalidCount = 0
    for i in range(0,10):
        txt = str(input("Enter value: "))
        step1 = int(txt[0]) + int(txt[2]) + int(txt[4])
        step2 = (int(txt[1])*3) + (int(txt[3])*3) + (int(txt[5])*3)
        checkDigit = int((step1 + step2) / 10)
        if checkDigit == 10:
            checkDigit = "X"
        if txt[6] == str(checkDigit):
            if Enqueue(txt[0:6]):   # characters 0-5, 6 not included
                print(f"{txt[0:6]} has been inserted.")
            else:
                print("Queue is full.")
        else:
            invalidCount += 1
       
    print(f"There were {invalidCount}, items")

# ii)
StoreItems()
item = Dequeue()
if item == False:
    print("Queue is empty") 
else:
    print(f"Item removed: {item}")

# iii)
# Enter value: 999999X
# 999999 has been inserted.
# Enter value: 1251484
# 125148 has been inserted.
# Enter value: 5500212
# 550021 has been inserted.
# Enter value: 0033585
# Enter value: 9845788
# 984578 has been inserted.
# Enter value: 6666666
# Enter value: 3258746
# Enter value: 8111022
# 811102 has been inserted.
# Enter value: 7568557
# 756855 has been inserted.
# Enter value: 0012353
# There were 4, items
# Item removed: 999999
