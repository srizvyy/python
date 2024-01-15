hello = "Hello World"

def reverse_string(str):
    return str[::-1]

# print(reverse_string(hello))

def reverse_string_two(str):
    result = ""
    for char in str:
        result = char + result
    return result

print(reverse_string_two(hello))
