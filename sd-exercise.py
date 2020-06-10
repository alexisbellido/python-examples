# input: 120
# output : 1   2   1

# input: 1220

# output:  1 2 2 1



# input: 807
# output: 808

#  1  8  3  3  8  1 double-ended queue

# 1 2 1 1


from collections import deque


def is_palindrome(x):
    d = deque(str(x))
    if len(d) == 1:
        return True
    head = d.popleft()
    tail = d.pop()
    # print(f'Test 1 - head {head} tail {tail}')
    # print('d', d)
    # print('len', len(d))
    while len(d) >= 1:
        if head != tail:
            return False
        else:
            if len(d) > 1:
                head = d.popleft()
                tail = d.pop()
            else:
                return False
            # print(f'Test 2 - head {head} tail {tail}')
            if head != tail:
                return False
    return True

def get_next_pal(num):
    x = num + 1
    while not is_palindrome(x):
        print('current x', x)
        x += 1
    return x

if __name__ == '__main__':
    # num = 120
    # print(get_next_pal(num))

    num = 801
    print(get_next_pal(num))
    # num = 808
    # print(num, is_palindrome(num))

    # num = 1
    # print(num, is_palindrome(num))

    # num = 802
    # print(num, is_palindrome(num))

    # num = 1211
    # print(num, is_palindrome(num))

    # num = 123321
    # print(num, is_palindrome(num))

