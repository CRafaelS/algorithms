def count_char_string(word):
    dict_first_string = dict()
    for letra in word:
        if letra in dict_first_string:
            dict_first_string[letra] += 1
        else:
            dict_first_string[letra] = 1
    return dict_first_string


def is_anagram(first_string, second_string):

    len_first_string = count_char_string(first_string.casefold())
    len_second_string = count_char_string(second_string.casefold())

    if len(first_string) != len(second_string):
        return False

    if len_first_string == len_second_string:
        return True
    return False
