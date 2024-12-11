def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    return sum(numbers) / len(numbers)

# Example usage with potential error:
data = [10, 20, 30, 'a']
average = calculate_average(data)
print(f"The average is: {average}")

#Example with a correct list
data2 = [10,20,30,40]
average2 = calculate_average(data2)
print(f"The average is: {average2}")