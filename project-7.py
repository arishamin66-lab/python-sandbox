import random

# Pick a secret number between 1 and 10
num = random.randint(1, 10)

guessed_correctly = False

for a in range(1, 6):
    print("You have " + str(6 - a) + " attempts")
    b = int(input("Enter your number between 1-10: "))
    if b == num:
        # BUG FIX: the original code set `a = 6` here, intending to end the
        # game, but reassigning a for-loop's variable has no effect on the
        # loop itself - it gets overwritten on the next iteration anyway.
        # The `break` right after it was what actually stopped the loop,
        # so the `a = 6` line did nothing useful and has been removed.
        guessed_correctly = True
        print("You guessed correct")
        break
    elif b > num:
        print("You guessed higher")
    else:
        print("You guessed lower")

# IMPROVEMENT: let the player know if they ran out of attempts without
# guessing correctly, and reveal the number.
if not guessed_correctly:
    print(f"Out of attempts! The number was {num}")
