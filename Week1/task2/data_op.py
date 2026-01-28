# data_op.py

numbers = [10, 20, 20, 40, 50, 10, 60]

# Remove duplicates
unique_numbers = list(set(numbers))

# Sorting
sorted_numbers = sorted(unique_numbers)

# Calculations
maximum = max(sorted_numbers)
minimum = min(sorted_numbers)
average = sum(sorted_numbers) / len(sorted_numbers)

print("Original:", numbers)
print("Unique:", unique_numbers)
print("Sorted:", sorted_numbers)
print("Max:", maximum)
print("Min:", minimum)
print("Average:", average)
