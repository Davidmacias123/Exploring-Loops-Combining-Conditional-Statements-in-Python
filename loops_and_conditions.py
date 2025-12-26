usernames = ["david123",
             "david456",
             "admin",
             "david999",
             "david000"
             ]
for username in usernames:
    if username == "admin":
        print("Welcome Administrator")
    else:
        print("You are not the administrator")


    
    attempts = 1

    while attempts <= 3:
        print(f"login attempt {attempts}")
        attempts = attempts + 1
        if attempts >= 4:
            print("access locked")
    
    
    
login_times = [7, 10, 13, 18, 22]

for login_time in login_times:
    if login_time >= 9 and login_time <= 17:
        print("Access during business hours")
    elif login_time < 9:
            print("Early Access- flag for review")
    else:
       print("After hours -notify security")
    