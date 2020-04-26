#sample input : 3 4 6
x = list(map(int, input("Enter the dimentions: ").split()))
list1, list2, list3 = [], [], []

# to create a list haviing 6 no of "*"
for i in range(0,x[2]):
    list1.append('*')

# to create a list containing 4 instances of the previous list
for j in range(0,x[1]):
    list2.append(list1)

# to create a list containing 3 instances of the previous list
for k in range(0,x[0]):   
    list3.append(list2)

#to remove the quotes around the list elements
translation = {39: None}
print(str(list3).translate(translation))
