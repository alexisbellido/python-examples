if __name__ == '__main__':
    # x = int(input("Enter a number\n"))

    # word = ''
    # while word != 'stop':
    #     word = input("Enter a word\n")
    #     print(word)

    points = {
        'A+': 4.0,
        'A': 4.0,
        'A-': 3.67,
        'B+': 3.33,
        'B': 3.0,
    }

    done = False
    while not done:
        grade = input()
        if grade == '':
            done = True
        else:
            print('points for grade {}: {}'.format(grade, points[grade]))
