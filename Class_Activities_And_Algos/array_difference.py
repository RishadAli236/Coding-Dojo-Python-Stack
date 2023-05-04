# def array_diff(list_a, list_b):
#     for value in list_b:
#         for i in range (len(list_a)):
#             if value in list_a:
#                 list_a.remove(value)
#             length = len(list_a)
#     return list_a

# print(array_diff([1,2,2,2,3,2,3,2,4,5,4,6,5,2,3,3,4,5,2,3,4], [2,3,4]))

def array_diff(list_a, list_b):
    for value in list_b:
        while value in list_a:
                list_a.remove(value)
    return list_a

print(array_diff([1,2,2,2,3], [2]))

# def array_diff(list_a, list_b):
#     new_list = list_a[:]
#     for list_b_value in list_b:
#         for list_a_value in list_a:
#             if list_b_value == list_a_value:
#                 new_list.remove(list_a_value)
#     return new_list

# print(array_diff([1,2,2,2,3,2,3,2,4,5,4,6,5,2,3,3,4,5,2,3,4], [2,3,4]))