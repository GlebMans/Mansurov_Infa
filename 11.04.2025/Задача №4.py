input_string = input()
def convert(input_string):
    if len(input_string) < 4:
        if input_string.isupper():
            return input_string.upper()
        else:
            return input_string
    else:
        uppercase_count = sum(1 for char in input_string[:4] if char.isupper())
        if uppercase_count >= 3:
            return input_string.upper()
        else:
            return input_string

print(convert(input_string))