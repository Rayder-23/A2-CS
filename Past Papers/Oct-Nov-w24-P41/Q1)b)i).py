def ReadData():
    arr:str = []
    for i in range(45):
        data = open('Data.txt')
        arr = data.read().split()
        data.close()
    return arr


# Part B(i)

def FormatArray(array):
    b:str = ""
    for i in range(len(array)):
        a = array.pop()
        b = f"{b} {a}"
    return b

test = ReadData()
print(FormatArray(test))