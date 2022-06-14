def shortest_repeating(string: str) -> int:
    string_len_half = int(len(string))/2

    for idx, letter in enumerate(string):
        if idx == string_len_half:
            return len(string)

        letter_split = string[:idx+1]
        letter_list = string.split(letter_split)
        empty_check = all(v == '' for v in letter_list)

        if empty_check:
            return int(len(letter_split))


if __name__ == '__main__':
    test_cases = ['ababab', 'aaaaa', 'abc']
    for item in test_cases:
        result = shortest_repeating(item)
        print(f'Output: {result}')
