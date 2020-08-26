red = {'s1', 's2', 's3', 'b3', 'c3', 'p1', 'd2', 'b2'}
blue = {'d1', 'p1', 's2', 's4', 'p2', 'd2', 's3', 'p3'}
star = {'c2', 'c3', 'd1', 'p1', 'p2', 'd2', 'b1', 'b2'}
led = {'p3', 'd3', 's3', 'b3', 'd2', 'b2', 'p2', 'b1'}

code = {
    'r': red,
    'b': blue,
    's': star,
    'l': led,
}


if __name__ == '__main__':
    print('Enter the features of wire present, e.g. "rbs". Features absent '\
          'need not to be entered. If no feature present, press ENTER without '\
          'entering anything. Enter "exit" to quit the program.')
    print('\tr: red')
    print('\tb: blue')
    print('\ts: star')
    print('\tl: LED')

    while True:
        wire_features = input('Enter features of wire: ')

        # exit command
        if wire_features == 'exit':
            break

        if not wire_features:
            print('Cut the wire.')
            continue

        temp = red | blue | star | led
        for feature in code.keys():
            if feature in wire_features:
                temp = temp & code[feature]
            else:
                temp = temp - code[feature]

        assert len(temp) == 1
        ans = list(temp)[0][0]
        if ans == 'c':
            print('Cut the wire.')
        elif ans == 'd':
            print('Do not cut the wire.')
        elif ans == 's':
            print('Cut the wire if the last digit of the serial number is even.')
        elif ans == 'p':
            print('Cut the wire if the bomb has a parallel port.')
        elif ans == 'b':
            print('Cut the wire if the bomb has two or more batteries.')