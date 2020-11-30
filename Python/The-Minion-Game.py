from string import whitespace


def minion_game(string):

    consonant_count = 0
    vowel_count = 0
    str_len = len(string)
    for i in range(str_len):
        if string[i] in "AEIOU":
            vowel_count += (str_len)-i
        else:
            consonant_count += (str_len)-i

    if vowel_count > consonant_count:
        print("Kevin", vowel_count)
    elif consonant_count > vowel_count:
        print("Stuart", consonant_count)
    else:
        print("Draw")
