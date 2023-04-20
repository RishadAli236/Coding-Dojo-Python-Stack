# Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

def move_zeros(num_list):
    for i in range(len(num_list)):
        if num_list[i] == 0:
            zero = num_list.pop(i)
            num_list.append(zero)
    return num_list

print(move_zeros([1, 0, 1, 2, 0, 1, 3])) # returns [1, 1, 2, 1, 3, 0, 0]



