fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  
#2
for x in "banana":
  print(x)
  
#3
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

#4
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
  
  
#5
for x in range(6):
  print(x)
  
#6
for x in range(2, 6):
  print(x)
  
#7
for x in range(2, 30, 3):
  print(x)

#8
for x in range(6):
  print(x)
else:
  print("Finally finished!")
  
#9
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")
  
#10
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)