def reverse_string(s):
    reverse_str = ""
    for char in s:
        reverse_str= char + reverse_str
    return reverse_str
print(reverse_string("Hello"))        