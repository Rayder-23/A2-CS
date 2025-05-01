# 2) Queue
# FIFO, First In, First Out
# Insert = EnQueue -> at Tail
# Remove = DeQueue -> at Head
# Circular Queues, they loop

queue = [None]*10
numitems = 0
headp = -1  # start at -1 as the start of the array is 0
tailp = -1

def enqueue(item):
    global numitems, tailp
    if (numitems >= 10):    # check if queue is full
        print("Queue is Full.")
    else:
        tailp = tailp +1    # moves the pointer one position forward
        if (tailp > 9):     # this is what makes it circular, if it exceeds 9 then it goes back to 0
            tailp = 0

        queue[tailp] = item # puts the item at that one forward position
        numitems = numitems +1  #adds to the tally

print(queue)
enqueue("Hamza")
enqueue("Hamza")
enqueue("Hamza")
print(queue)

headp = 0   # changed otherwise it would be outside the list
def dequeue():
    global numitems, headp, tailp
    if (numitems > 0):
        item = queue[headp]     # picks the top value
        queue[headp] = None  # removes that value
        numitems = numitems -1  # removes from the tally
        if (numitems == 0): # queue empty, reset headp and tailp
            headp = -1
            tailp = -1
        else:
            headp = headp +1    # queue not empty, moves headp
            if (headp > 9): # makes queue circular
                headp = 0
    else:
        print("Queue is Empty.")
    return item

print(dequeue())
print(queue)