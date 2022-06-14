def shortest_repeating(string: str) -> int:
    final_result = None

    for idx, letter in enumerate(string):
        letter_split = string[:idx+1]
        result = string.split(letter_split)
        result_len = len(result)
        counter = 0
        if idx+1 == len(string):
            final_result = len(string)
            break
        for checker in result:
            if checker == '':
                counter += 1
            else:
                break
        if counter == result_len:
            repeating = letter_split
            final_result = len(repeating)
            break
    print('bye')
    return int(final_result)


if __name__ == '__main__':
    test_str = "abc"
    result = shortest_repeating(test_str)
    print(result)