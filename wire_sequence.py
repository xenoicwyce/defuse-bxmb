red = {
    1: 'c', 2: 'b', 3: 'a',
    4: 'ac', 5: 'b', 6: 'ac',
    7: 'abc', 8: 'ab', 9: 'b',
}

blue = {
    1: 'b', 2: 'ac', 3: 'b',
    4: 'a', 5: 'b', 6: 'bc',
    7: 'c', 8: 'ac', 9: 'a',
}

black = {
    1: 'abc', 2: 'ac', 3: 'b',
    4: 'ac', 5: 'b', 6: 'bc',
    7: 'ab', 8: 'c', 9: 'c',
}


if __name__ == '__main__':
    print('Enter the wire color and the alphabet it connects to, in each ' \
          'panel, e.g. "ra, bb, kc". Enter "exit" to quit the program.')
    print('\tr: red wire')
    print('\tb: blue wire')
    print('\tk: black wire')

    red_count, blue_count, black_count = 0, 0, 0
    panel_num = 1
    while panel_num < 5:
        wires = input('Panel {}: '.format(panel_num)).lower()
        wires = [w.strip() for w in wires.split(',')]

        # exit command
        if wires == 'exit':
            break

        ## input clarity check
        # check length
        if not all(map(lambda w: len(w) == 2, wires)):
            print('Format is incorrect. Please check and try again.')
            continue

        # check color
        if not all(map(lambda w: w[0] in 'rbk', wires)):
            print('Color is incorrect. Please check and try again.')
            continue

        # check port
        if not all(map(lambda w: w[1] in 'abc', wires)):
            print('Port is incorrect. Please check and try again.')
            continue

        for wire in wires:
            color, port = wire
            if color == 'r':
                red_count += 1
                if port in red[red_count]:
                    print('Cut red.')
                else:
                    print('Ignore red.')

            elif color == 'b':
                blue_count += 1
                if port in blue[blue_count]:
                    print('Cut blue.')
                else:
                    print('Ignore blue.')

            elif color == 'k':
                black_count += 1
                if port in black[black_count]:
                    print('Cut black.')
                else:
                    print('Ignore black.')

        panel_num += 1