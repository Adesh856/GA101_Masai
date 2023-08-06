# # Exercise 1: Extract Substrings
# # Given a string text, extract the following substrings using slicing:

# # Extract the first 4 characters.
# # Extract the last 5 characters.
# # Extract the characters from index 3 to index 8.

text = "Hello, World!"

print(text[:4])
print(text[-5:])
print(text[3:8])


# Sure! Let's explain the slicing example `text = "Hello, World!"; slice_result = text[::2]` in bullet points:

# - `text = "Hello, World!"`: This line assigns the string "Hello, World!" to the variable `text`.
# - `slice_result = text[::2]`: This line uses slicing notation to create a new string called `slice_result`.

# The slicing notation has the following format: `string[start:end:step]`. In this case, the slicing arguments are as follows:

# - `start`: Not specified, so it defaults to the beginning of the string (`0`).
# - `end`: Not specified, so it defaults to the end of the string (up to the last character).
# - `step`: Set to `2`, which means every second character will be included in the slice.

# Here's how the slicing works step by step:

# 1. The `start` index is `0` (not specified), which corresponds to the first character "H".
# 2. The `end` index is not specified, so it goes up to the end of the string, which is the exclamation mark "!".
# 3. The `step` value is `2`, so every second character is included in the slice.
# 4. Characters at even positions (0, 2, 4, ...) are included, while characters at odd positions (1, 3, 5, ...) are skipped.

# Resulting `slice_result` string: "HloWrd"

# Explanation:
# - The characters at even positions in the original string are: "H", "l", "o", "W", "r", and "d".
# - All other characters (",", "e", "l", ",", " ", "o", "!" in positions 1, 3, 5, 7, 9, and 11) are skipped.

# So, the final `slice_result` is "HloWrd". The slicing operation skipped every second character, resulting in a new string with only the characters at even positions from the original string.

  


# # Exercise 2: Reverse List
# # Given a list my_list, reverse the order of the elements using slicing.
# text = "Hello, World!"
# print(text[-5::-1])

# # Exercise 3: Extract Sublists
# # Given a list my_list, extract the following sublists using slicing:

# # Extract the first 3 elements.
# # Extract the last 2 elements.
# print(text[:3])
# print(text[-2:])
# # Sure! Please let me know which topic you would like to learn about next. We can cover various Python topics, such as:

# # 1. String Manipulation
# # 2. File Handling
# # 3. Object-Oriented Programming (OOP) in Python
# # 4. Error Handling (Exceptions)
# # 5. List Comprehensions
# # 6. Generators and Iterators
# # 7. Decorators
# # 8. Working with Dates and Times (Datetime module)
# # 9. Regular Expressions (re module)
# # 10. Python Standard Library modules (random, math, os, etc.)

# # Or any other specific topic you are interested in. Just let me know, and we can start exploring it!