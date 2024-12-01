# In this project, you are going to build a program that takes a camelCase or PascalCase
# formatted string as input and converts that to a snake_case formatted string using two approaches. 

# In Python, a list comprehension is a construct that allows you to generate a new list by applying an expression to each item in an existing iterable and optionally filtering items with a condition. Apart from being briefer, list comprehensions often run faster.

# A basic list comprehension consists of an expression followed by a for clause:

# Example Code
# spam = [i * 2 for i in iterable]
# The above uses the variable i to iterate over iterable. Each elements of the resulting list is obtained by evaluating the expression i * 2 at the current iteration.

# In this step, you need to fill the empty list snake_cased_char_list using the list comprehension syntax.

# Turn your empty list into a list comprehension that converts each character in pascal_or_camel_cased_string into a lowercase character and prepends an underscore to it (the code you commented out before may help you write the expression). Use char to iterate over pascal_or_camel_cased_string.


#     # return clean_snake_cased_string

# Code 

# def convert_to_snake_case(pascal_or_camel_cased_string):
#     # snake_cased_char_list = []
#     # for char in pascal_or_camel_cased_string:
#     #     if char.isupper():
#     #       converted_character = '_' + char.lower()
#     #       snake_cased_char_list.append(converted_character)
#     #     else:
#     #         snake_cased_char_list.append(char)
#     # snake_cased_string = ''.join(snake_cased_char_list)
#     # clean_snake_cased_string = snake_cased_string.strip('_')

#     # return clean_snake_cased_string

#     snake_cased_char_list = []
#     return ''.join(snake_cased_char_list).strip('_')

# def main():
#     print(convert_to_snake_case('aLongAndComplexString'))

# main()

def convert_to_snake_case(pascal_or_camel_cased_string):

    snake_cased_char_list = [
        '_' + char.lower() if char.isupper()
        else char
        for char in pascal_or_camel_cased_string
    ]

    return ''.join(snake_cased_char_list).strip('_')

def main():
    print(convert_to_snake_case('IAmAPascalCasedString'))


main()