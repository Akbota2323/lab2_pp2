thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

#2
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

#3
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

#4
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

#5
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

#6
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

#7
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

#8
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

#9
thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)

#10
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

#11
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)
