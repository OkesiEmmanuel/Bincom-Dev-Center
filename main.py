import re
import requests
from collections import Counter
import statistics
from db import save_colors_to_db
from utils import (
    generate_random_binary, fibonacci_sum, recursive_search, calculate_variance, calculate_probability
)

# Step 1: Fetch and parse webpage content
url = ''
response = requests.get(url)
web_content = response.text

# Step 2: Extract color data using regular expression. colors can be added in the color patterns
color_pattern = r'\b(red|blue|green|yellow|black|white)\b'
colors = re.findall(color_pattern, web_content, re.IGNORECASE)

# Normalize to lowercase
colors = [color.lower() for color in colors]

# Count frequency of each color
color_counter = Counter(colors)
print("Color frequencies:", color_counter)

# Step 3: Calculate the most worn color
most_worn_color = color_counter.most_common(1)[0][0]
print("Most worn color:", most_worn_color)

# Step 4: Calculate mean color
mean_color = most_worn_color
print("Mean color:", mean_color)

# Step 5: Calculate the median color
sorted_colors = sorted(colors)
median_color = statistics.median(sorted_colors)
print("Median color:", median_color)

# Step 6: Variance of colors
variance = calculate_variance(colors)
print("Variance of colors:", variance)

# Step 7: Probability of red
probability_red = calculate_probability('red', color_counter, len(colors))
print(f"Probability of red: {probability_red:.2f}")

# Step 8: Save colors to PostgreSQL
save_colors_to_db(color_counter)

# Step 9: Random 4-digit binary number and base 10 conversion
binary_number, decimal_number = generate_random_binary()
print(f"Random binary: {binary_number}, Decimal: {decimal_number}")

# Step 10: Fibonacci sequence sum
fib_sum = fibonacci_sum(50)
print("Sum of first 50 Fibonacci numbers:", fib_sum)

# Step 11: Recursive search
numbers = [1, 3, 5, 7, 9, 11, 13]
target = int(input("Enter a number to search: "))
found = recursive_search(numbers, target, 0, len(numbers) - 1)
if found:
    print(f"{target} found in the list.")
else:
    print(f"{target} not found in the list.")
