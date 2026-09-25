users = {
    "ali": "1234",
    "ahmed": "abcd",
    "sara": "pass123"
}

user = input("Enter your username: ").strip().lower()
password = input("Enter your password: ").strip()

userN = False
for key in users.keys():
    if userN is False:
        if user == key:
            userN = True

userp = False

if userN is True:
    for value in users.values():
        if userp is False:
            if users[user] == value and users[user] == password:
                userp = True
else:
    print("Your username is invalid")

if userN is True and userp is False:
    print("Password is invalid")
    
if userp is True and userN is True:
    print("login successful")