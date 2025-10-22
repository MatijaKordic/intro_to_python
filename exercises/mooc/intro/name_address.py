# Please write a program which asks for the user's name and address.
# The program should also print out the given information, as follows:
# Steve Sanders
# 91 Station Road
# London EC05 6AW
# Write your solution here
given_name = input("What is your name?")
family_name = input("What is your family name?")
address = input("What is your street address?")
city = input("What is your city and postal code?")

print(f"{given_name} {family_name}")
print(address)
print(city)