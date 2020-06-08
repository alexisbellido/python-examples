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

    min_birth = 2999
    max_death = 0

    for p in people:
        birth = p[0]
        death = p[1]
        print('birth', birth)
        print('death', death)
        print('-----------')
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
        print(f'year: {year}, count: {count}')
        if count >= max_alive:
            max_alive = count
            year_max_alive = year
    
    print(f'year_max_alive {year_max_alive} max_alive {max_alive}')



        