str1 = input()
str2 = input()
def combine(str1, str2):
    reverse_str1 = str1[:2][::-1] + str1[2:]
    reverse_str2 = str2[:2][::-1] + str2[2:]
    result = f"{reverse_str1}-{reverse_str2}"
    return result

print(combine(str1, str2))