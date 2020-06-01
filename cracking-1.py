def is_unique(str):
    """check if string contains all unique characters, assume just 128 ASCII characters"""
    char_list = [False] * 128
    if len(str) > 128:
        return False
    for c in str:
        if char_list[ord(c)]:
            # found character in list
            return False
        # set True for index with the numeric value of this character in list
        char_list[ord(c)] = True
    return True

def are_permutations(s, t):
    if len(s) != len(t):
        return False
    s_list = list(s)
    s_list.sort()
    t_list = list(t)
    t_list.sort()
    return s_list == t_list

if __name__ == "__main__":

    print('ord("A")', ord("A"), 'chr(65)', chr(65))

    str = "abc"
    print(str, is_unique(str))

    str = "xyyz"
    print(str, is_unique(str))

    s = "cat"
    t = "horse"
    print(s, t, are_permutations(s, t))

    s = "dog"
    t = "god"
    print(s, t, are_permutations(s, t))

    s = "cat"
    t = "god"
    print(s, t, are_permutations(s, t))

    s = "ratona"
    t = "tonara"
    print(s, t, are_permutations(s, t))