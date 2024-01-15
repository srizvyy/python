# Algorithm: Run Length Encoding 

# given a string input 'wwwwwwbbbwwwww' 
# give a out w6b3w5

str_one = "wwwwwwbbbwwwww"

# reason for using len(input_str) - 1 in the loop
# it's trying to access input_str[i+1] in the last iteration of the loop, which leads to an "IndexError" because there is no character at the position i+1 in the last iteration.

def runLengthEncoding(input_str):
    counter = 0
    result = ""
    for i in range(len(input_str) - 1):
        counter += 1
        if input_str[i] != input_str[i+1]:
            result += input_str[i] + str(counter)
            counter = 0
    # add last char to result and update counter by 1
    result += input_str[-1] + str(counter + 1)
    return result 
    

print(runLengthEncoding(str_one))






