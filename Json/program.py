# JSON
# JSON (JavaScript Object Notation) is a lightweight text format for exchanging data. Python’s json module serializes Python objects to JSON strings and deserializes JSON back to Python. It is built into the standard library and requires no installation. 

# JSON Type	Example

# Object	{"a": 2, "b": 4}
# Array	[2, 4, 6, 8]
# String	"hello"
# Number	42, 2.46
# Boolean	true, false
# Null	null 


# Python to JSON Type Mapping 

# The json module maps Python types to JSON types in a fixed way. 
# Not every Python type has a direct JSON equivalent. 

# Python Type	JSON Type
# dict	object
# list, tuple	array
# str	string
# int, float	number
# bool	boolean
# None	null

import json
 
data = {"a": 2, "b": 4, "c": [6, 8], "d": None, "e": True}
s = json.dumps(data)
print(s)  # {"a": 2, "b": 4, "c": [6, 8], "d": null, "e": true}

# Serialize: json.dumps()

# json.dumps(obj) converts a Python object to a JSON string. The result is a str, not bytes.
import json
 
data = {"x": 2, "y": 4, "z": 6}
s = json.dumps(data)
print(s)           # {"x": 2, "y": 4, "z": 6}
print(type(s))     # <class 'str'> 

# Deserialize: json.loads() 

# json.loads(s) parses a JSON string and returns a Python object. 
# The input must be a str or bytes (decoded as UTF-8).

import json
 
s = '{"a": 2, "b": 4, "c": [6, 8]}'
data = json.loads(s)
print(data)        # {'a': 2, 'b': 4, 'c': [6, 8]}
print(type(data))  # <class 'dict'>