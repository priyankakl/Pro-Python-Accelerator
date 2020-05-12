dict1 = {}
list1 = []
list2 =[]
dict2 = {}
sentence = input("Enter the sentence:")

# To split the sentence into words and form a list
list_of_words = sentence.split(" ")


for word in list_of_words: 
    # if word has more than one occurance in the sentence, increase its count by 1 each time
    if(word in dict1.keys()):
        dict1[word] = dict1[word] + int(1)
    # if its the first occurance of a word, then keep the count as 1
    else:
        dict1[word] = int(1)

# separate out numbers, special characters, and alphabets to make sorting easy
for i in dict1.keys():
    if ((i.isnumeric() )or (not i.isalpha())):
        list1.append(i)
    else:
        list2.append(i)

# sort both the lists
list1.sort()
list2.sort()

# add both the list1 and list2 data into new dictionary and print
for j in list1:
    dict2[j] = dict1[j]
for k in list2:
    dict2[k] = dict1[k]
for p, q in dict2.items():
    print(p + ":" + str(q))


 
    