mydict = {"hello" : "world", "speckbit":"self-learning", "life":"meaning"}

# take input from the user
var = input("enter the value who's key you want to know: ")

# to get the index of the given value
for x in mydict.values():
    if x == var:
        pointer = list(mydict.values()).index(x)
    else:
        pass

# to get the key with the help of index
result = list(mydict.keys())[pointer]

print(result)
