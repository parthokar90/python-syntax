# An iterator in Python is an object that contains a countable number of values and allows you to traverse through them one by one.

# Under the hood, an iterator implements two methods, known as the iterator protocol:

# __iter__(): Returns the iterator object itself.

# __next__(): Returns the next element in the sequence. Raises a StopIteration exception when no more elements are left.

# Note: Iterables (like lists, tuples, and strings) can be converted into iterators using the iter() function.


# Converting a list (iterable) into an iterator
fruits = ["apple", "banana", "cherry"]
fruit_iterator = iter(fruits)

# Fetching items one by one using next()
print(next(fruit_iterator))  # Output: apple
print(next(fruit_iterator))  # Output: banana
print(next(fruit_iterator))  # Output: cherry

# Calling next() again raises StopIteration error
# print(next(fruit_iterator))  # Raises StopIteration

#Creating a Custom Iterator Class

class CountDown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        val = self.current
        self.current -= 1
        return val

# Using the custom iterator in a for loop
for num in CountDown(3):
    print(num)  # Output: 3, then 2, then 1
