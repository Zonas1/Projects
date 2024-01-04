mylist = ["apple","banana","Orange","Mango","Grapes","Pineapple"]
print(mylist)
mylist.remove("apple")
print(mylist)
mylist.append("apple")
print(mylist)
for x in mylist:
    print(x)

for i in range(len(mylist)):
    print(mylist[i])
i = 0
while i < len(mylist):
    print(mylist[i])
    i = i+1
mylist.sort(reverse=True)
print(mylist)