# A data type is a classification that specifies the kind of values a variable can hold and the operations that can be performed on those values.Python is a dynamically typed language, meaning you don't explicitly declare the data type of a variable; Python infers it based on the value assigned.

# 1. Numeric Types:
    # int (Integer): Whole numbers (e.g., 5, -100, 0).
    # float (Floating-point number): Real numbers with a decimal point (e.g., 3.14, -0.5, 2.0).
    # complex (Complex number): Numbers with a real and an imaginary part (e.g., 2 + 3j).

# 2. Sequence Types:
    # str (String): Ordered sequences of characters, enclosed in single or double quotes (e.g., "hello", 'Python').
    # list (List): Ordered, mutable collections of items, enclosed in square brackets (e.g., [1, 2, "apple"]). Lists can contain items of different data types.
    # tuple (Tuple): Ordered, immutable collections of items, enclosed in parentheses (e.g., ("red", "green", "blue")). Once created, tuples cannot be modified.
    # range: Represents an immutable sequence of numbers, often used in loops (e.g., range(5) generates numbers from 0 to 4).

# 3. Set Types:
    # set (Set): Unordered collections of unique items, enclosed in curly braces (e.g., {1, 2, 3}). Sets do not allow duplicate elements.
    # frozenset (Frozen Set): Immutable versions of sets.

# 4. Mapping Type:
    # dict (Dictionary): Unordered collections of key-value pairs, enclosed in curly braces (e.g., {"name": "Alice", "age": 30}). Keys must be unique and immutable.

# 5. Boolean Type:
    # bool (Boolean): Represents truth values, either True or False. Used for logical operations.

# 6. None Type:
    # NoneType: Represents the absence of a value or a null value, represented by the keyword None.


# Explicit Type Conversion (Type Casting)
    # Explicit type conversion, also known as type casting, involves the programmer explicitly converting a value from one data type to another using built-in functions. This provides more control over the conversion process and is necessary when Python cannot implicitly convert types or when a specific type is required.

    # Common functions for explicit type conversion include:
        # int(): Converts a value to an integer.
        # float(): Converts a value to a float.
        # str(): Converts a value to a string.
        # list(): Converts an iterable to a list.
        # tuple(): Converts an iterable to a tuple.

num = 10
# print(type(num)) # <class 'int'>
# fnum = float(num)
# print(type(fnum)) # <class 'float'>

# num1 = 34.5
# print(int(num1))
# print(type(int(num1)))

# Implicit Type Conversion (Coercion)
    # Implicit type conversion, also known as coercion, occurs automatically when Python needs to perform an operation involving different data types. Python attempts to convert one data type to another without explicit instructions from the programmer, usually promoting a "smaller" or "less precise" data type to a "larger" or "more precise" one to avoid data loss.

# num1 = 10
# num2 = 24.6
# num3 = num1 + num2
# print(num3)