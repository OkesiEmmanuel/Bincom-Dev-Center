#import the libraries needed for the operations
import random
import statistics

# Calculate variance of colors (color to numerical mapping for variance calculation)
color_mapping = {
    'red': 1, 'blue': 2, 'green': 3, 'yellow': 4, 'black': 5, 'white': 6
}

def calculate_variance(colors):
    color_values = [color_mapping[color] for color in colors]
    variance = statistics.variance(color_values)
    return variance

# Calculate the probability of a specific color
def calculate_probability(color, color_counter, total_colors):
    color_count = color_counter.get(color, 0)
    probability = color_count / total_colors
    return probability

# Generate random 4-digit binary number and convert to decimal
def generate_random_binary():
    binary_number = ''.join(random.choice(['0', '1']) for _ in range(4))
    decimal_number = int(binary_number, 2)
    return binary_number, decimal_number

# Recursive search algorithm
def recursive_search(arr, target, low, high):
    if low > high:
        return False
    mid = (low + high) // 2
    if arr[mid] == target:
        return True
    elif arr[mid] > target:
        return recursive_search(arr, target, low, mid - 1)
    else:
        return recursive_search(arr, target, mid + 1, high)

# Sum of first n Fibonacci numbers
def fibonacci_sum(n):
    def fibonacci_sequence(n):
        a, b = 0, 1
        for _ in range(n):
            yield a
            a, b = b, a + b

    return sum(fibonacci_sequence(n))
