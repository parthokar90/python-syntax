# Try / Except
# In Python, try / except blocks are used for exception handling. They allow your program to gracefully catch and process runtime errors instead of
# crashing or displaying a raw error trace to the user.

def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        return None
    except TypeError:
        print("Error: Inputs must be numbers.")
        return None
    else:
        # Runs ONLY if no exceptions were raised
        print("Calculation successful!")
        return result
    finally:
        # Runs ALWAYS (useful for cleanup like closing files/connections)
        print("Division check complete.")

# Testing the function
safe_divide(10, 2)   # Success case
safe_divide(10, 0)   # Triggers ZeroDivisionError 



# When to Use try / except

# User Input Validation: When handling unpredictable input (e.g., converting a string typed by a user into an integer).

# External I/O Operations: When performing operations that can fail due to external factors, such as reading files, querying databases, or making HTTP API requests.

# Type Conversion & Parsing: When parsing formats like JSON, XML, or timestamps where malformed data could break the parser.

# Why to Use try / except (Key Advantages)

# Prevents Program Crashes: Keeps your server, script, or application running smoothly even when an unexpected operational error occurs.

# User-Friendly Error Messages: Replaces intimidating traceback errors with clear, actionable messages for the user or helpful error logs for developers.

# Guaranteed Resource Cleanup: The finally clause ensures critical resource releases (closing file streams, shutting down network sockets) occur regardless of success or failure.