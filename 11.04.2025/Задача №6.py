input_string = input()
def ASCII(input_string):
    length = len(input_string)
    if length <= 2:
        return ord(input_string[0])
    elif 2 < length < 10:
        first = ord(input_string[0])
        last = ord(input_string[-1])
        middle_index = (length - 1) // 2
        middle = ord(input_string[middle_index])
        return first + middle + last
    else:
        return ord(input_string[-1])

print(ASCII(input_string))