# List of dictionaries
list_of_dicts = [
    {'id': 1, 'name': 'apple'},
    {'id': 2, 'name': 'mango'},
    {'id': 3, 'name': 'grape'},
]

# Specific ID to filter
specific_id = 1

# Using filter with lambda function to filter dictionaries
filtered_dict = list(filter(lambda x: x['id'] == specific_id, list_of_dicts))

# Display the result
print("Filtered dictionary:", filtered_dict)