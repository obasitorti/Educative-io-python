def is_unique(input_str):
    # input_str = input_str.replace(" ", "")
    # input_str = input_str.lower

    uniq = set()
    for i in input_str:
        if i in uniq:
            return False
        uniq.add(i)
    return True

input_str = "abcdefg"
result = is_unique(input_str)
print(f"The string '{input_str}' is unique: {result}")
