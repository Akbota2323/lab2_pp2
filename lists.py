thislist = ["apple", "banana", "cherry"]
print(thislist)

#2
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

#3
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
print(list1)
print(list2)
print(list3)

#4
mylist = ["apple", "banana", "cherry"]
print(type(mylist))

#5
thislist = list(("apple", "banana", "cherry")) 
print(thislist)

#6
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

#7
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

#8
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

#9
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

#10
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

#11
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

#12
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

#13
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#14
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#15
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#16
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

#17
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

#18
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

#19
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])
  
#20

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1
  
#21
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

#22
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if x != "apple"]

print(newlist)


#23
newlist = [x for x in range(10) if x < 5]

#24
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x.upper() for x in fruits]

print(newlist)

#25
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = ['hello' for x in fruits]

print(newlist)