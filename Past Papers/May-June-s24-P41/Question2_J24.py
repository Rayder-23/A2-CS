# Part 1
class Tree:
    def __init__(self,name:str,growth:int,height:int,width:int,Evergreen):
        self.__TreeName = name
        self.__HeightGrowth = growth
        self.__MaxHeight = height
        self.__MaxWidth = width
        self.__Evergreen = Evergreen

    def GetTreeName(self):
        return self.__TreeName
    def GetMaxHeight(self):
        return self.__MaxHeight
    def GetMaxWidth(self):
        return self.__MaxWidth
    def GetGrowth(self):
        return self.__HeightGrowth
    def GetEvergreen(self):
        return self.__Evergreen
    # def __str__(self):
    #     return f"Tree(Name: {self.__TreeName}, Growth: {self.__HeightGrowth}, MaxHeight: {self.__MaxHeight}, MaxWidth: {self.__MaxWidth}, Evergreen: {self.__Evergreen})"

    
# Part B
def ReadData():
    tree = []
    try:
        file = open('Trees.txt', 'r')
        for line in file:
            # strip removes whitespaces
            # splits elements that are separated
            fields = line.strip().split(',')
            name = fields[0]
            growth = int(fields[1])
            height = int(fields[2])
            width = int(fields[3])
            evergreen = fields[4] 
            tree.append(Tree(name,growth,height,width,evergreen))
        return tree
    except FileNotFoundError:
        print("File not found.")


# Part C

def PrintTrees(tree):
    if tree.GetEvergreen() == "Yes":
        print(f"{tree.GetTreeName()} has max height {tree.GetMaxHeight()}, a maximum width {tree.GetMaxWidth()} and grows {tree.GetGrowth()}cm. It does not lose its leaves.")
    else:
        print(f"{tree.GetTreeName()} has max height {tree.GetMaxHeight()}, a maximum width {tree.GetMaxWidth()} and grows {tree.GetGrowth()}cm. It loses its leaves each year.")

# Part D
test = ReadData()
# PrintTrees(test[0])
# PrintTrees(test[3])

def ChooseTree(tree):
    userArray = []
    maxh = int(input("Enter Max Height in cm: "))
    maxw = int(input("Enter Max Width in cm: "))
    green = str(input("Enter Evergreen (Yes/No): "))
    count = 0

    for i in tree:
        if i.GetMaxHeight() <= maxh and i.GetMaxWidth() <= maxw and i.GetEvergreen() == green:
            userArray.append(i)
            count += 1
        
    if count == 0:
        print("No valid trees.")
    else:
        for tree in userArray:
            PrintTrees(tree)

        # Part C        
        name = str(input("Enter name of Tree: "))
        height = int(input("Enter height in cm: "))
        years = 0
        for tree in userArray:
            if name == tree.GetTreeName():
                while height < tree.GetMaxHeight():
                    height += tree.GetGrowth()
                    years += 1
                print(years)

# Part C) iii)
ChooseTree(test)
# Enter Max Height in cm: 400
# Enter Max Width in cm: 200
# Enter Evergreen (Yes/No): Yes
# Blue Conifer has max height 250, a maximum width 50 and grows 40cm. It does not lose its leaves.  
# Green Conifer has max height 300, a maximum width 150 and grows 40cm. It does not lose its leaves.
# Enter name of Tree: Blue Conifer
# Enter height in cm: 100
# 4