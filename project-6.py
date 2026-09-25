users = {
    "ali": "1234",
    "ahmed": "abcd",
    "sara": "pass123"
}

user = input("Enter your username: ").strip().lower()
password = input("Enter your password: ").strip()

# Check whether the username exists
userN = user in users

if not userN:
    print("Your username is invalid")

# SIMPLIFICATION: the original code looped over every value in the
# dictionary comparing it to the stored password on each iteration
# (`for value in users.values(): if users[user] == value and users[user] == password`).
# That loop was redundant work: since users[user] is a single fixed value,
# the whole check reduces to a direct comparison against the entered
# password. It still worked, but this version is simpler and does the same
# thing without the unnecessary loop.
userp = False
if userN:
    userp = users[user] == password

    if not userp:
        print("Password is invalid")
    else:
        print("login successful")
