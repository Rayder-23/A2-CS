# --- STRING FUNCTIONS ---

text = "Cambridge A Level Computer Science"

# 1. split(separator) - Splits string into a list
words = text.split(" ")  # ['Cambridge', 'A', 'Level', 'Computer', 'Science']

# 2. join(list) - Joins list of strings into one string
joined = " ".join(words)  # 'Cambridge A Level Computer Science'

# 3. lower() - Converts to lowercase
lower_text = text.lower()  # 'cambridge a level computer science'

# 4. upper() - Converts to uppercase
upper_text = text.upper()  # 'CAMBRIDGE A LEVEL COMPUTER SCIENCE'

# 5. find(substring) - Finds first index of substring
position = text.find("Level")  # 12

# 6. replace(old, new) - Replaces all old with new
new_text = text.replace("Science", "Studies")  # 'Cambridge A Level Computer Studies'

# 7. strip() - Removes whitespace (or characters) from both ends
line = "  Hello, World!  "
stripped = line.strip()  # 'Hello, World!'
custom_strip = "###Python###".strip("#")  # 'Python'