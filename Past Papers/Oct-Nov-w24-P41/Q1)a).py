# Part A

def ReadData():
    arr:str = []
    for i in range(45):
        data = open('Data.txt')
        arr = data.read().split()
        data.close()
    return arr

print(ReadData())