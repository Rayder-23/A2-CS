name = "Haris Basil Hamza"

print(len(name))   # 17
print(name[:])  # [lb:up], will print whole name

#left to right: +ve value
print(name[:5]) # "Haris"
print(name[12:18]) # "Hamza"
print(name[6:11]) # "Basil"

#right to left: -ve value
print(name[-5:]) # "Hamza"
# print(name[-5:6]) # will give error, both have to be negative

count = 0
for x in range(len(name)):  
   # print(name[x:x +1]) # will print every character individually 
   ch = name[x:x+1]
   if (ch == "A") or (ch == "a"):
      count = count +1
print(count)