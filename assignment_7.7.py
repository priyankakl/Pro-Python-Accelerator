my_list1 = eval(input("Enter the list with elements:"))
my_list2 = []
n = int(input("Enter the value of 'n' to find nth lowest in the list:"))
my_list1.sort()

# To remove duplicate elements in the first list by sending only unique elements to the second list
for element in my_list1:
    if element not in my_list2:
        my_list2.append(element)
    else:
        pass

print(str(n) + "the lowest number is:" + str(my_list2[n-1]) )

    




