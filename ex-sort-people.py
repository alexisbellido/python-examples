import operator
import pprint


if __name__ == '__main__':
    print("\n")

    data = [
        ['4', '21', '1', '14', '2008-10-24 15:42:58'],
        ['3', '22', '4', '2somename', '2008-10-24 15:22:03'],
        ['5', '21', '3', '19', '2008-10-24 15:45:45'],
        ['6', '21', '1', '1somename', '2008-10-24 15:45:49'],
        ['7', '22', '3', '2somename', '2008-10-24 15:45:51']
    ]

    pprint.pprint(data)
    print("\n")

    data.sort(key=operator.itemgetter(1))
    pprint.pprint(data)
    print("\n")

    # ages = [-2, 10, -5, -11, 90, -14, 20, 15, 13, 105, 3]
    # pprint.pprint(ages)
    #
    # # sorted function returns a new sorted list
    # sorted_ages = sorted(ages)
    # pprint.pprint(sorted_ages)
    #
    # # sort method sorts in place
    # ages.sort()
    # pprint.pprint(ages)
    #
    # ages.sort(key=abs)
    # pprint.pprint(ages)
