# list of banned users
"""
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")
"""

age = input("Enter age here. ")
age = int(age)

if age >= 18:
    print("You are old enough to vote. \nHave you registered to vote yet?")
else:
    print("Sorry, you are too young to vote. \nPlease register to vote as soon as you turn 18!")