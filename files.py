user_name = input("Enter your name: ")
age = input("Enter your age: ")
dob = input("Enter your date of birth (YYYY-MM-DD): ")
file_content = f"User Name: {user_name}\nAge: {age}\nDate of Birth: {dob}"
with open("user", "w") as file:
    file.write(file_content)
print(f"User information saved to user.txt")
