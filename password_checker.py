"""
CP1404 Password Checker
"""

MIN_LENGTH = 4
password = input("Enter Password: ")
while len(password) < MIN_LENGTH:
    print("Invalid password")
    password = input("Enter Password: ")
print("*" * len(password))