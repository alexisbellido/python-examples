import operator

def person_lister(f):
    def inner(people):
        # sorted_people = sorted(people, key=operator.itemgetter(2), reverse=False)
        # people.sort(key=operator.itemgetter(2), reverse=False)
        # # print(sorted_people)
        print(people)
        # for person in people:
        #     return f(person)
        # return f(people)
        # return f(people[0])
        # print(people)
        return f(people)
        # complete the function
    return inner

@person_lister
def name_format(person):
    # return(person)
    # return(person[0])
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1] + " - " + person[2]

if __name__ == '__main__':
    # people = [input().split() for i in range(int(input()))]
    # print(*name_format(people), sep='\n')

    ####################
    people = [
        ['Mike', 'Thomson', '20', 'M'],
        ['Another', 'Bustle', '32', 'M'],
        ['Child', 'Kid', '5', 'M'],
        ['Robert', 'Bustle', '32', 'M'],
        ['Andria', 'Bustle', '30', 'F'],
    ]
    # print(name_format(people[0]))
    # print(name_format(people[1]))
    # print(name_format(people[2]))
    # print(name_format(people[3]))
    # print(name_format(people[4]))
    print(*name_format(people), sep='\n')

    # print(people)

    # num = 3
    # input_data = [
    #     'After Robert 32 M',
    #     'Mike Thomson 20 M',
    #     'Robert Bustle 32 M',
    #     'Andria Bustle 30 F',
    # ]
    # input_data.sort(key=operator.itemgetter(2), reverse=True)
    # people = [row.split() for row in input_data]
