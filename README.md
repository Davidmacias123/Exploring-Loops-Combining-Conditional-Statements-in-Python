# loops_and_conditions.py — Access Control with Loops & Conditions (Python)

## On-the-Job Scenario (what this is simulating)
You’ve been asked to help automate **access control** for a secure folder based on:
- **user role** (example: “admin” vs normal user)
- **number of login attempts**
- **time of access** (business hours vs early/after-hours)

This project is a practice script that prints messages that represent what a real system *might* do.

---

## Challenge Steps (what this script demonstrates)

### Step 1–2: Setup
1. Launch **Anaconda Navigator**
2. Open **Spyder IDE**
3. Create a new Python script named: **`loops_and_conditions.py`**

### Step 3: For loop + list of usernames
You will:
- Create a **list of five usernames**
- Use a **for loop** to print a custom message for each user
- Inside the loop, check:
  - If the username is exactly `"admin"`, print a special message

### Step 4: While loop + counter (login attempts)
You will:
- Set `attempts = 1`
- Use a **while loop** that runs while `attempts <= 3`
- Print the attempt number each time
- Increase attempts each loop (increment)
- After the loop ends, print **“Access locked”** if the max attempts were reached

### Step 5: Combine loop + if/elif/else for login times
You will:
- Create a list of login times like `[7, 10, 13, 18, 22]`
- Loop through each time and decide:
  - 9–17 → **“Access during business hours.”**
  - before 9 → **“Early access – flag for review.”**
  - after 17 → **“After hours – notify security.”**

---

## The code you should use (clean, correct, matches the steps)

> Note: Your uploaded code has the right ideas, but your `attempts` **while loop is indented inside the username for-loop**, which causes it to run 5 times (once for each username).  
> This version places Step 4 **separately**, which is what the job aid describes. (Your original content is shown in your upload.)

```python
# Step 3: List + for loop + condition
usernames = ["david123", "david456", "admin", "david999", "david000"]

for username in usernames:
    # If the username is exactly "admin", show a special message
    if username == "admin":
        print("Welcome Administrator")
    else:
        print(f"Welcome, {username}")

print()  # blank line for readability

# Step 4: While loop + attempts counter
attempts = 1

while attempts <= 3:
    print(f"Login attempt {attempts}")
    attempts = attempts + 1  # increment (add 1)

# After the loop ends, attempts will be 4, meaning max attempts were reached
print("Access locked")

print()  # blank line for readability

# Step 5: Loop through login times + if/elif/else
login_times = [7, 10, 13, 18, 22]

for login_time in login_times:
    if login_time >= 9 and login_time <= 17:
        print("Access during business hours.")
    elif login_time < 9:
        print("Early access – flag for review.")
    else:
        print("After hours – notify security.")
```

---

## Explain it like you’re 5 👶 (super simple)

### Big idea
Imagine a **door** that decides what to say when people try to enter.

### Step 3 (usernames)
- We have a **list** of names (like a class list).
- We look at **each name** one by one.
- If the name is `"admin"`, we say **“Welcome Administrator”** (special VIP).
- If it’s not admin, we say **“Welcome, (name)”**.

### Step 4 (attempts)
- We count login tries: 1, 2, 3.
- After 3 tries, we say **“Access locked”** (the door locks).

### Step 5 (login times)
- We check what time someone logged in.
- If it’s **9 to 17**, it’s normal work time → “business hours”.
- If it’s **before 9**, it’s early → “flag for review”.
- If it’s **after 17**, it’s late → “notify security”.

---

## Every single line explained (line-by-line)

### Step 3: usernames list + for loop
- `usernames = [...]`
  - Makes a **list** (a group) of 5 usernames.

- `for username in usernames:`
  - Means: “For **each** name in the list, do the next indented lines.”

- `if username == "admin":`
  - Ask: “Is this username exactly the word `admin`?”

- `print("Welcome Administrator")`
  - If yes, print a special admin message.

- `else:`
  - If the username is **not** admin, do this instead.

- `print(f"Welcome, {username}")`
  - Prints “Welcome,” plus the actual username.
  - The `f"..."` is an **f-string** which lets you put variables inside `{}`.

- `print()`
  - Prints a blank line to make the output easier to read.

### Step 4: while loop (attempts)
- `attempts = 1`
  - Start counting at 1.

- `while attempts <= 3:`
  - Keep looping while attempts is 1, 2, or 3.

- `print(f"Login attempt {attempts}")`
  - Show the attempt number.

- `attempts = attempts + 1`
  - Increase attempts by 1 each loop (1→2→3→4).

- `print("Access locked")`
  - After the loop ends (after 3 tries), print that access is locked.

### Step 5: login times + if/elif/else
- `login_times = [7, 10, 13, 18, 22]`
  - A list of times (hours in 24-hour format).

- `for login_time in login_times:`
  - Look at each time one by one.

- `if login_time >= 9 and login_time <= 17:`
  - If time is between 9 and 17 (inclusive), it’s business hours.
  - `and` means **both** parts must be true.

- `elif login_time < 9:`
  - Else if the time is earlier than 9, it’s early access.

- `else:`
  - Otherwise it must be after 17, so it’s after-hours.

---

## Your original code (for reference)
This is what you uploaded (shown here so you can compare). fileciteturn2file0L1-L31

---

## Author
David Macias
