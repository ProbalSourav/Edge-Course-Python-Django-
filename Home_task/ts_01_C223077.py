#                         string manipulation

# 1. Concatenation of two strings
a = "Hello"
b = "World"
print("#1 Concatenation:", a+" "+b)

# 2. Repeating a string multiple times
repeat_str = "Repeat"
print("#2 Repeating a string:", repeat_str * 3)

# 3. Checking if a substring exists within a string
main_str = "This is a string"
print("#3 Checking substring:","This" in main_str)

# 4. Converting string to uppercase
print("#4 Uppercase:", main_str.upper())  # Output: THIS IS A STRING

# 5. Converting string to lowercase
print("#5 Lowercase:", main_str.lower())  # Output: this is a string

# 6. Capitalizing the first letter of the string
print("#6 Capitalized:",main_str.capitalize()) # Output: This is a string

# 7. Swapping case of all characters
print("#7 Swap case:",main_str.swapcase())# Output: tHIS IS A STRING

# 8. Finding the index of a substring
print("#8 Finding index of 'string':", main_str.find('a'))  # Output: 10

# 9. Replacing a part of a string
print("#9 Replacing a part of a string:",main_str.replace("string","text"))

# 10. Counting occurrences of a substring
print("#10 Counting the occurance of a substring:",main_str.count("is")) # Output: 2

# 11. Checking if a string starts with a specific substring
print("#11 Starts with 'This':",main_str.startswith("This"))  # Output: True

# 12. Checking if a string ends with a specific substring
print("#12 Ends with 'string':", main_str.endswith("string"))  # Output: True

# 13. Stripping whitespace from both ends
white_space="        Hello there    "
print("#13 Stripping whitespace:",white_space.strip())    #Output: "Hello there"

# 14. Stripping only leading whitespace
print("#14 Left strip:", white_space.lstrip())       # Output: "Hello there    "

# 15. Stripping only trailing whitespace
print("#15 Right strip:", white_space.rstrip())  # Output: "   Hello there"

# 16. Splitting a string by spaces
print("#16 Splitting by spaces:", main_str.split())  # Output: ['This', 'is', 'a', 'string']

# 17. Splitting a string by a specific delimiter
csv_str="apple,banana,grape"
print("#17 Splitting by comma:",csv_str.split(','))# Output: ['apple', 'banana', 'grape']

# 18. Joining a list of strings with a delimiter
list_of_fruits=['apple','banana','grape']
print("#18 Joining with comma:", "," .join(list_of_fruits)) # Output: apple,banana,grape

# 19. Getting the length of a string
print("#19 Length of string:", len(main_str))  # Output: 16

# 20. Checking if all characters are alphabetic
alpha_str = "HelloWorld"
print("#20 All alphabetic:", alpha_str.isalpha())  # Output: True

# 21. Checking if all characters are digits
num_str = "12345"
print("#21 All digits:", num_str.isdigit())  # Output: True

# 22. Checking if a string is alphanumeric (letters and digits only)
alnum_str = "Hello123"
print("#22 Alphanumeric:", alnum_str.isalnum())  # Output: True

# 23. Checking if a string contains only whitespace
empty_str = "   "
print("#23 Only whitespace:", empty_str.isspace())  # Output: True

# 24. Converting string to title case
title_str = "this is a title"
print("#24 Title case:", title_str.title())  # Output: This Is A Title

# 25. Padding a string to the left
padded_left = "5".rjust(3, '0')
print("#25 Left padding with zeros:", padded_left)  # Output: 005

# 26. Padding a string to the right
padded_right = "5".ljust(3, '0')
print("#26 Right padding with zeros:", padded_right)  # Output: 500

# 27. Centering a string with padding
centered_str = "Centered".center(20, '-')
print("#27 Centering with padding:", centered_str)  # Output: -----Centered-----

# 28. Checking if a string is in title case
print("#28 Is title case:", title_str.istitle())  # Output: False

# 29. Converting integer to string
num = 100
print("#29 Integer to string:", str(num))  # Output: '100'

# 30. Converting float to string
float_num = 100.55
print("#30 Float to string:", str(float_num))  # Output: '100.55'

# 31. Checking if string is numeric
print("#31 Is numeric:", "12345".isnumeric())  # Output: True

# 32. Encoding a string to bytes
encoded_str = main_str.encode('utf-8')
print("#32 Encoding string to bytes:", encoded_str)  # Output: b'This is a string'

# 33. Decoding bytes back to string
decoded_str = encoded_str.decode('utf-8')
print("#33 Decoding bytes to string:", decoded_str)  # Output: This is a string

# 34. Formatting a string using f-strings
name= "Probal"
age=23
print(f"#34 F-string format: {name} is {age} years old")

# 35. Using str.format method
print("#35 Using format method:","{} is {} years old.".format(name,age))

# 36. Accessing characters by index
print("#36 Character at index 1:", main_str[1])  # Output: h

# 37. Slicing a string (substring)
print("#37 Slicing substring:", main_str[0:4]) # Output: This

# 38. Reversing a string using slicing
print("#38 Reversing string:", main_str[::-1])  # Output: gnirts a si sihT

# 39. Checking if string is printable
print("#39 Is printable:", "Hello\n".isprintable())  # Output: False

# 40. Finding the last occurrence of a substring
print("#40 Last occurrence of 'is':", main_str.rfind("is"))  # Output: 5

# 41. Checking if string is in lowercase
print("#41 Is lowercase:", main_str.islower())  # Output: False

# 42. Checking if string is in uppercase
print("#42 Is uppercase:", main_str.isupper())  # Output: False

# 43. Z-filling a string (adding leading zeros)
zfill_str = "-7"
print("#43 Zero filling:", zfill_str.zfill(8))  # Output: 00007

# 44. Formatting with thousands separator
num_large = 1234567890
print("#44 Formatting with commas:", "{:,}".format(num_large))  # Output: 1,234,567,890

# 45. Finding the minimum character
print("#45 Minimum character in 'abc':", min("abc"))  # Output: a

# 46. Finding the maximum character
print("#46 Maximum character in 'abc':", max("abc"))  # Output: c

# 47. Removing a prefix
print("#47 Removing prefix:", "Prefix_string".removeprefix("Prefix_"))  # Output: string

# 48. Removing a suffix
print("#48 Removing suffix:", "string_suffix".removesuffix("_suffix"))  # Output: string

# 49. Splitting string by lines
multiline_str = "Line 1\nLine 2\nLine 3"
print("#49 Splitting by lines:", multiline_str.splitlines() )

# 50. Checking if string is a valid identifier
print("#50 Is valid identifier:", "variable_name".isidentifier())  # Output: True