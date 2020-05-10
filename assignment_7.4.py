dict1 = {}
list1 = []
list2 =[]
dict2 = {}
sentence = input("Enter the sentence:")
list_of_words = sentence.split(" ")
for word in list_of_words: 
    if(word in dict1.keys()):
        dict1[word] = dict1[word] + int(1)
    else:
        dict1[word] = int(1)

for i in dict1.keys():
    if ((i.isnumeric() )or (not i.isalpha())):
        list1.append(i)
    else:
        list2.append(i)
list1.sort()
list2.sort()
for j in list1:
    dict2[j] = dict1[j]
for k in list2:
    dict2[k] = dict1[k]
for p, q in dict2.items():
    print(p + ":" + str(q))


 
    