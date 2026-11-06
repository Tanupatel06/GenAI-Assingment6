def check_age(age):
    if age < 1 or age > 120:
        raise ValueError("Age must be between 1 and 120")

try:
    age = int(input("Enter your age: "))
    check_age(age)
    print("Age is valid.")

except ValueError as e:
    print("Error:", e)