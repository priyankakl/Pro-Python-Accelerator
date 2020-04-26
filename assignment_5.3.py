name = ""
print("Enter 3 names in 3 lines")

# to take input in 3 lines
for x in range(0,3): 
    name = name + input() + "\n"

# converting each line of input into list elements
name = name.split("\n")

for x in range(0,3):
    result = ""
    # check if name contains only alphabets
    if not name[x].isalpha():
        for y in name[x]:
            # check if each character is an alphabet or space. Only then add it to result
            if y.isalpha() or y == " " :
                result = result + y
            else:
                pass
        # to check if name contains only special chracters or numbers or both     
        if len(result) == 0:
            print("you have entered a name with only special characters and numbers")
        print(result)
    else: 
        print(name[x])
    
