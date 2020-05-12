import math

# take input from the user
moves = input("how many moves would you like to give?:")

# initialize the coordinates to 0 in the beginning
x1, x2, y1, y2 = 0, 0, 0, 0

# update the coordinate values according to the input
for i in range(int(moves)):
    (a,b) = eval(input("Enter the move as a tuple:"))
    if a == "UP":
        y2 = y2 + int(b)
    elif a == "DOWN":
        y2 = y2 - int(b)
    elif a == "LEFT":
        x2 = x2 - int(b)
    else: 
        x2 = x2 + int(b)

# calculate the distance with the formulae
distance = math.sqrt(((x2 - x1)**2) + ((y2 - y1)**2))

print("distance",int(distance))