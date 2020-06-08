def brute_force(people):
    min_birth = 2999
    max_birth = 0
    # no need for max_death as that will only decrement population
    max_death = 0

    for p in people:
        birth = p[0]
        death = p[1]
        if birth < min_birth:
            min_birth = birth
        if death > max_death:
            max_death = death
    print('min_birth', min_birth, 'max_death', max_death)

    years_count = {}
    for year in range(min_birth, max_death + 1):
        for p in people:
            birth = p[0]
            death = p[1]
            if birth <= year <= death:
                years_count[year] = years_count.get(year, 0) + 1

    year_max_alive = None
    max_alive = 0
    for year, count in years_count.items():
        # print(f'year: {year}, count: {count}')
        if count >= max_alive:
            max_alive = count
            year_max_alive = year
    
    print(f'year_max_alive {year_max_alive} max_alive {max_alive}')

def get_min_max_births(people):
    min_birth = 2999
    max_birth = 0
    return min_birth, max_birth

def get_deltas(people):
    deltas = []
    return deltas

def get_max_year(people):
    deltas = get_deltas(people)
    min_birth, max_birth = get_min_max_births(people)
    # print(f'min_birth {min_birth}, max_birth {max_birth}')
    return 0

if __name__ == "__main__":
    people = [
        (1920, 1980),
        (1930, 1950),
        (2001, 2035),
        (1820, 1901),
        (1930, 2035),
        (2001, 2022),
        (1980, 1984),
        (1984, 1986),
    ]

    # brute_force(people)

    max_year = get_max_year(people)
    print('max_year', max_year)

    # somethig more efficient only checking years when something happens, birth or death
    # write as functions in a modular way by creating array of deltas first
    # adding 1 to a year for a birth and decreasing 1 from year for a death.
    # Note it may be better to use an array so that the indexes can be used as the actual year
    # by playing with an offset
    # see https://vimeo.com/158532188
    # print("-------")
    # years_set = set()
    # years_count_2 = {}
    # for p in people:
    #     birth = p[0]
    #     # deaths decrement the population so no need to check those years
    #     # death = p[1]
    #     years_set.add(birth)
    #     # years_set.add(death)
    #     # print('birth', birth, 'death', death)
    #     # print('-----------')

    # # years_set = sorted(years_set) # do I need to turn set into a sorted list?
    # # print('years_set', years_set)
    # for year in years_set:
    #     print('year to check', year)





        