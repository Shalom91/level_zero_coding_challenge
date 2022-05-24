def maximum(*arguments):
    """
    returns the maximum number
    *arguments: integer arguments e.g. 1,22,3,2
    """
    maximum_number = 0
    *create_list, = arguments 
    duplicate_list = [i for i in create_list]
    list_of_small_numbers = [i for i in create_list for j in duplicate_list if i < j]
    for i in duplicate_list:
        if i not in list_of_small_numbers:
            maximum_number = i
    return maximum_number


        