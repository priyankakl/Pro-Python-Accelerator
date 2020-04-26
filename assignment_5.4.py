print("Enter 2 sentences in 2 lines")
sentence = ""

# to take input in 2 lines
for x in range(0,2): 
    sentence = sentence + input() + "\n"

# converting each line of input into list elements
sentence = sentence.split("\n")

for i in range(0,len(sentence)-1):
    for x in range(0,(len(sentence[i]))):
        if sentence[i][x].isupper():
            if x == 0:
                result = sentence[i][x]
            else:   
                result = result + " " + sentence[i][x]
        else:
            result = result + sentence[i][x]
    print(result) 
    result = ""

