# Simple Python Variables, Constants, and Print

# Constants
PI=3.14
MAX_SCORE = 100
ACCOUNT_LIMIT_USD =2000
WITHDRAWAL_LIMIT_USD = 1000.00

print(WITHDRAWAL_LIMIT_USD ," daily withdrawal limit")
print("During this program, account limit usd is a constant with value:",ACCOUNT_LIMIT_USD)

# Variables (can change during program)
name = "Paidamoyo Masunda"
age = 35
score = 95
is_passing = True

# Using the print function
print("=== Basic Print Examples ===")
print("student age:", age)
print("student name:", name)

# Print with variables
print("=== Using Variables ===")
print(f"Hi, my name is {name}")
print(f"I am {age} years old")
print(f"My test score is {score}/{MAX_SCORE}")
print(f"Am I passing? {is_passing}")

# Print with constants
print("=== Using Constants ===")
print(f"The value of PI is {PI}")

# Simple calculation
circle_radius = 5
area = PI * circle_radius * circle_radius
print(f"Area of circle with radius {circle_radius}: {area}")

# Showing how variables can change
print("\n=== Variables Can Change ===")
print(f"Score started as: {score}")

score = score + 5  # Add 10 points
print(f"After bonus: {score}")

score = 100  # Set to new value
print(f"Final score: {score}")

# Changing other variables
print(f"\nName was: {name}")
name = "Paidamoyo Hapanga"
age = 35
print(f"Name is now: {name}")

age = age + 1  # Birthday!
print(f"After birthday, age is: {age}")

# Constants should not change
print(f"\nWithdrawal limit should stay: {WITHDRAWAL_LIMIT_USD}")