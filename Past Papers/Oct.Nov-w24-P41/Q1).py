# Part A
def ReadData():
    arr:str = []
    for i in range(45):
        data = open('Data.txt')
        arr = data.read().split()
        data.close()
    return arr
# print(ReadData())


# Part B(i)
def FormatArray(array):
    b:str = ""
    for i in range(len(array)):
        a = array.pop()
        b = f"{b} {a}"
    return b
# print(FormatArray(ReadData()))


# Part B(ii)
test = ReadData()
print(FormatArray(test))

# link to paper:
# https://pastpapers.papacambridge.com/viewer/caie/as-and-a-level-computer-science-for-first-examination-in-2021-9618-2024-oct-nov-9618-w24-ms-32-pdf-9618-w24-ms-33-pdf-9618-w24-ms-41-pdf-9618-w24-ms-42-pdf-9618-w24-ms-43-pdf-9618-w24-qp-11-pdf-9618-w24-qp-12-pdf-9618-w24-qp-13-pdf-9618-w24-qp-21-pdf-9618-w24-qp-22-pdf-9618-w24-qp-23-pdf-9618-w24-qp-31-pdf-9618-w24-qp-32-pdf-9618-w24-qp-33-pdf-9618-w24-qp-41-pdf