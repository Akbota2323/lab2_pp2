print(10 > 9)
print(10 == 9)
print(10 < 9)

#2
a = 200
b = 33
if(b > a):
    print("b is greater than a")
else:
    print("b is not greater than a ")
    
#3
print(bool("Hello"))
print(bool(15))

#4
print(bool("abc"))
print(bool(123))
print(bool(["apple","cherry","banana"]))

#5
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))      

#6
class myclass():
    def _len_(self):
        return 0
myobj = myclass()
print(bool(myobj))

#7
def myfunction():
    return True
print(myfunction())

#8
def myFunction():
    return True
if myFunction():
    print("YES!")
else:
    print("NO!")
    
#9
x = 100
print(isinstance(x,int))
    