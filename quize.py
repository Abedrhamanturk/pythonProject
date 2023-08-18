def is_palindrome(number):
    number_str = str(number)
    return number_str == number_str[::-1]
def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
while True:

    print("Menu:")
    print("1. Check if a number is palindrome")
    print("2. Check if a number is even or odd")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        num = int(input("Enter a number: "))
        if is_palindrome(num):
            print(f"{num} is a palindrome!")
        else:
            print(f"{num} is not a palindrome.")
    elif choice == '2':
        num = int(input("Enter a number: "))
        result = check_even_odd(num)
        print(f"{num} is {result}.")
    elif choice == '3':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please choose 1, 2, or 3.")


