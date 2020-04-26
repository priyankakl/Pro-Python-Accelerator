import sys
count = input("Enter number of students: ")
print("Enter the student name along with marks")
mydict = {"name": [], "math": [], "physics": [], "chemistry": [], "biology": [], "social-science" :[]}

for i in range(0, int(count)):
    list1 = input().split()
    mydict["name"].append(list1[0])
    mydict["math"].append(list1[1])
    mydict["physics"].append(list1[2])
    mydict["chemistry"].append(list1[3])
    mydict["biology"].append(list1[4])
    mydict["social-science"].append(list1[5])

print("Enter the student name along with the subject: ")

def find():
    while True:
        var = input().split()
        if var[0] in mydict["name"]:
            for x in mydict["name"]:
                if var[0] == x:
                    pointer = mydict["name"].index(x) 
                else:
                    pass
            marks = mydict[var[1]][pointer]    
            print(f"{var[0]} scored {marks} in {var[1]}")
        else:
            break
find()

subject = input("Enter subject: ")
x = 0
x = int(x)
for y in mydict[subject]:
    print(f"{mydict['name'][x]} {y}")
    x = x+1







