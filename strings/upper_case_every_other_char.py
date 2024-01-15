str_one = "saim"

def upperCaseEveryOtherChar(str):
    char_list = [char for char in str]
    result = ""
    for i, char in enumerate(char_list):
        if i % 2 == 1:
            char_list[i] = char.upper()
    return result.join(char_list)
        

print(upperCaseEveryOtherChar(str_one))