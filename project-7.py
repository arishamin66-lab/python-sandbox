import random

num = random.randint(1,10)

for a in range(1,6):
    print("You have " + str(6-a) + " attempts")
    b = int(input("Enter your number between 1-10: "))
    if b == num:
        a = 6
        print("You guessed correct")
        break
    elif b > num:
        print("You guessed higher")
    else:
        print("You guessed lower")
    
