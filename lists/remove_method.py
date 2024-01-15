my_list = [1,2,3,4,5,6]

for i in my_list:
    my_list.remove(i)

print(my_list)


# Here's what happens during each iteration:

# Iteration 1: Removes the element at index 0 (value 1).
# Iteration 2: Removes the element at index 1 (value 3, note that the original element at index 1, which was 2, is now at index 0 due to the removal in the previous iteration).
# Iteration 3: Removes the element at index 2 (value 5, note that the original element at index 2, which was 4, is now at index 1 due to the removal in the previous iteration).