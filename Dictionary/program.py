# A Python dictionary is a mutable, key-value paired collection written with curly braces {} and colons :. Keys must be unique and immutable (such as strings, numbers, or tuples), 
# while values can be of any data type and can repeat.

# Creating a dictionary
user_profile = {
    "username": "coder123",
    "email": "user@example.com",
    "age": 25,
    "is_active": True
}

# Accessing and updating values
print(user_profile["username"])  # Output: coder123
user_profile["age"] = 26          # Updating existing key
user_profile["city"] = "Dhaka"    # Adding new key-value pair

# Safe retrieval using .get() to avoid KeyError
role = user_profile.get("role", "Guest")
print(role)  # Output: Guest


# When to Use Dictionaries

# Labeled / Structured Records: When representing real-world entities that have named properties, such as a user profile, a product item, or API response data (similar to JSON).

# Counting or Frequency Mapping: When keeping track of occurrences of items, like counting word frequencies in a text.

# Fast Value Lookup by Identifier: When you need to quickly locate data using a custom name or ID instead of an index position.

# Why to Use Dictionaries (Advantages over Lists and Tuples)

# Fast Retrieval: Looking up a value by its key runs in O(1) constant average time, making search operations instant even in large datasets.

# Readable and Self-Documenting: Accessing elements via meaningful keys (e.g., product["price"]) makes code much easier to read and maintain than using positional index numbers (e.g., product[1]).