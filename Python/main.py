import os 
if os.path.exists("john.txt"):
    os.remove("john.txt")
else:
    print("There is no file")