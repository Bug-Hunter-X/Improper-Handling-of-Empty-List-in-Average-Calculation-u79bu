def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list case
    total = sum(numbers)
    average = total / len(numbers)
    return average

#Example usage
my_numbers = [10, 20, 30, 40, 50]
average = calculate_average(my_numbers)
print(f"The average is: {average}")

my_empty_list = []
average = calculate_average(my_empty_list)
print(f"The average is: {average}")

#Example of the bug
my_numbers = []
result = calculate_average(my_numbers)
print(f"The average is: {result}") #This will print 0, but should raise a more informative exception
