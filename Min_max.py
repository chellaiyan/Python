import json

# Function to find the minimum start value and maximum end value
def find_min_max_values(filename):
    with open(filename, 'r') as file:
        data = json.load(file)

    # Initialize min_start and max_end with the first start and end values
    min_start = float('inf')
    max_end = float('-inf')

    # Iterate through the JSON data to find the min start and max end
    for item in data:
        min_start = min(min_start, item['start'])
        max_end = max(max_end, item['end'])

    return min_start, max_end

# Usage
filename = 'data.json'
min_start, max_end = find_min_max_values(filename)

print(f"Minimum Start Value: {min_start}")
print(f"Maximum End Value: {max_end}")
