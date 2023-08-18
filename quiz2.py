def find_smallest_largest(numbers):
    numbers.sort()
    smallest = numbers[0]
    largest = numbers[-1]
    return smallest, largest
input_numbers = [5, 2, 9, 1, 7, 3]
smallest, largest = find_smallest_largest(input_numbers)
print("Smallest:", smallest)
print("Largest:", largest)
