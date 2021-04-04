def print_vowels(string):
    """
    print all vowels in a string
    """
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowels_in_string = []
    lower_case_string = string.lower()
    for i in lower_case_string:
        if i in vowels:
            vowels_in_string.append(i)
    remove_duplicates = list(set(vowels_in_string))
    print(f"Vowels: {', '.join(letter for letter in remove_duplicates[::-1])}")


    