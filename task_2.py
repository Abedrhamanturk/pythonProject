full_name = input("Enter your Full Name: ")
mobile_number = input("Enter your Mobile Number (05x-xxxx-xxx): ")
year_of_birth = int(input("Enter your Year of Birth: "))
current_year = 2023
user_age = current_year - year_of_birth
mobile_number_list = mobile_number.split('-')
print("User Name:", full_name)
print("User Current Age:", user_age)
print("Mobile Number as a List:", mobile_number_list)