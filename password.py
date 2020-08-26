import copy

possible_ans = ['about', 'after', 'again', 'below', 'could',
                'every', 'first', 'found', 'great', 'house',
                'large', 'learn', 'never', 'other', 'place',
                'plant', 'point', 'right', 'small', 'sound',
                'spell', 'still', 'study', 'their', 'there',
                'these', 'thing', 'think', 'three', 'water',
                'where', 'which', 'world', 'would', 'write']


if __name__ == '__main__':
    initial_guess = copy.copy(possible_ans)
    for idx in range(5):
        given = input('Enter all possible character {}: '.format(idx+1)).lower()
        temp = list(filter(lambda word: word[idx] in given, initial_guess))
        print(temp)

        if len(temp) == 1:
            print('\nSearch concluded, answer: {}'.format(temp[0]))
            break
        elif len(temp) == 0:
            print('\nSearch concluded, no answer found.')
            break

        initial_guess = copy.copy(temp)