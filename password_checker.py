import re

password = input("Enter your password: ")

strength = 0

# Length check
if len(password) >= 8:
    strength += 1

# Number check
if re.search("[0-9]", password):
    strength += 1

# Uppercase check
if re.search("[A-Z]", password):
    strength += 1

# Special character check
if re.search("[!@#$%^&*(),.?\":{}|<>]", password):
    strength += 1

# Result
if strength <= 1:
    print("Password Strength: Weak")
elif strength == 2 or strength == 3:
    print("Password Strength: Medium")
else:
    print("Password Strength: Strong")
