def count_substring(string: str, substring: str):
    substrings_to_test = []
    for i in range(len(string)-len(substring)+1):
        substrings_to_test.append(string[i:i+len(substring)])
    return substrings_to_test.count(substring)
