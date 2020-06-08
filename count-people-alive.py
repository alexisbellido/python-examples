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

def get_first_last_births(people):
    first_birth = 2999
    last_birth = 0
    for p in people:
        birth = p[0]
        if birth < first_birth:
            first_birth = birth
        if birth > last_birth:
            last_birth = birth
    return first_birth, last_birth

def update_deltas(deltas, first_birth, last_birth, person):
    birth = person[0]
    birth_index = birth - first_birth
    print(f'birth {birth} - increment index {birth_index}')
    deltas[birth_index] += 1

    death = person[1]
    if (death + 1) <= last_birth:
        death_index = (death + 1) - first_birth
        print(f'year after death {death + 1} - decrement index {death_index}')
        deltas[death_index] -= 1

def get_deltas(people, first_birth, last_birth):
    # initialize deltas array with zeroes
    # considering an offset equal to first_birth
    deltas = [0] * (last_birth - first_birth + 1)
    for person in people:
        update_deltas(deltas, first_birth, last_birth, person)
    return deltas

def get_index_max_running_sum(deltas):
    running_sum = 0
    max_running_sum = 0
    peak_index = 0 # the index of the year with maximum population
    for index, count in enumerate(deltas):
        print(index, count)
        running_sum += count
        if running_sum > max_running_sum:
            max_running_sum = running_sum
            peak_index = index
    return peak_index, max_running_sum

def get_year_max_population(people):
    first_birth, last_birth = get_first_last_births(people)
    # print(f'first_birth {first_birth}, last_birth {last_birth}')
    deltas = get_deltas(people, first_birth, last_birth)
    # print(deltas)
    peak_index, max_running_sum = get_index_max_running_sum(deltas)
    return peak_index + first_birth, max_running_sum

if __name__ == "__main__":
    people = [
        # (1920, 1980),
        # (1930, 1950),
        # (2001, 2035),
        # (1820, 1901),
        # (1930, 2035),
        # (2001, 2022),
        # (1980, 1987),
        # (1979, 1987),
        # (1981, 1984),
        # (1982, 1985),
        # (1984, 1986),
        (1980, 1982),
        (1982, 1983),
        (1981, 1982),
        (1981, 1981),
    ]

    # brute_force(people)

    year_max_population, max_running_sum = get_year_max_population(people)
    print('year_max_population', year_max_population)
    print('max_running_sum', max_running_sum)

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





        