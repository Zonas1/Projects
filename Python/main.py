mydoc = {
    "Name" : "John",
    "Surname" : "Tharu",
    "Age" : "24",
    "School" : "Shree Pashupati Higher Secondary School",
    "College" : "Crimson College of Technology" 
}
mydoc["Age"] = 25
mydoc.update({"Age" : 26})
print(mydoc.items())