def calculate_average(numbers):
    if not numbers:
        raise ValueError("Cannot calculate the average of an empty list.")
    total = sum(numbers)
    average = total / len(numbers)
    return average

# Example usage
my_numbers = [10, 20, 30, 40, 50]
average = calculate_average(my_numbers)
print(f"The average is: {average}")

my_empty_list = []
try:
    average = calculate_average(my_empty_list)
    print(f"The average is: {average}")
except ValueError as e:
    print(f"Error: {e}") #This will print a ValueError exception
