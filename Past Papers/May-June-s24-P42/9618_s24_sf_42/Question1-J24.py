# Part A

def ReadWords(fileName:str):
    global WordArray
    global NumberWords
    WordArray = []
    with open(fileName, 'r') as file:
        for line in file:
            WordArray.append(line.strip())  # strip() removes newline characters
    NumberWords = len(WordArray)


# Part B

choice = input(str("Easy, Medium or Hard")).lower()
if choice == "easy":
    file = "Easy.txt"
elif choice == "medium":
    file = "Medium.txt"
elif choice == "hard":
    file = "Hard.txt"
ReadWords(file)

# Part C)i)

def Play():
    