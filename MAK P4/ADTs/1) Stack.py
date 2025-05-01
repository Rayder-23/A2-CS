# Abstract Data Types
# 1) Stack
# LIFO, Last In First Out
# TOS, Top of Stack
# Insert = PUSH
# Remove = POP

stack = [None]*10   # 0-9 elements, which are empty: None
tos = -1
# making a function
def push(item):
    global tos # defining tos as global, vscode might do this automatically
    if (tos < 9):
        tos = tos +1
        stack[tos] = item
    else:
        print("Stack is Full.")

print(stack)
push("Shahmir")
push("saba")
push("mohib")
print(stack)
print(" ")

def pop():
    global tos
    if (tos == -1):
        print("Stack is Empty.")
    else:
        item = stack[tos]
        stack[tos] = None
        tos = tos -1
        return item # should be in the else state, otherwise the item value is null & function doesn't work


print(pop())
print(pop())
print(pop())
pop()
pop()
print(stack)