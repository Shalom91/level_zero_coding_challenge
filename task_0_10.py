def common_letters(string_one, string_two):
    """
    prints out common letters between
    two strings
    """
    common_letters_list = []
    string_one, string_two = string_one.lower(), string_two.lower()
    for i in string_one:
        if i in string_two:
            common_letters_list.append(i)
    remove_duplicates = list(set(common_letters_list))
    print(f"Common letters: {', '.join(letter for letter in remove_duplicates)}")