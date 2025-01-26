thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)
#2
thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)

#3
myset = {"apple", "banana", "cherry"}
print(type(myset))
#4

thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

#5

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)
  
#6
thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)

#7
thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)

#8
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

#9
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

#10
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)

#11
thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)

#12
thisset = {"apple", "banana", "cherry"}

del thisset

print(thisset)

#13
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)
  
#14
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

#15
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1 | set2
print(set3)

#16
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

#17
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3)

#18
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 & set2
print(set3)

#19
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.intersection_update(set2)

print(set1)

#20
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)

print(set3)

#21
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 - set2
print(set3)

#22
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)

print(set3)

#23
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.symmetric_difference_update(set2)

print(set1)