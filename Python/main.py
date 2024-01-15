import re

txt = "My name is John kathariya Tharu and i am very bad boy"

x = re.search("^M.*y$",txt)
if x:
    print("You have a match")
else:
    print("You have no match")