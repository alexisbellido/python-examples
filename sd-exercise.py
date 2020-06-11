from collections import deque


def get_next_pal(num, is_palindrome_fn):
    try:
        p_num = num + 1
        while not is_palindrome_fn(p_num):
            # print('current num', p_num)
            p_num += 1
        return p_num
    except TypeError:
        return 0

# TODO
# def is_pal_math():
#     num = 807
#     temp=num
#     rev=0
#     while(num>0):
#         dig=num%10
#         rev=rev*10+dig
#         num=num//10
#         print('dig', dig)
#         print('rev', rev)
#         print('num', num)
#         print('====')
#     if(temp==rev):
#         print("The number is palindrome!")
#     else:
#         print("Not a palindrome!")

def is_pal_with_reverse(word):
    word_list = list(str(word)) # turn into string if it's a number
    if len(word_list) <= 1:
        return True
    # create a reverse list by cloning the original and running reverse() to reverse in place
    # reverse_word_list = word_list[:]
    # reverse_word_list.reverse()

    # create reverse list with list slicing
    reverse_word_list = word_list[::-1]
    return word_list == reverse_word_list

def is_pal_with_deque(word):
    d = deque(str(word))
    if len(d) <= 1:
        return True
    found = False
    while not found and len(d) > 1:
        head = d.popleft()
        tail = d.pop()
        if head != tail:
            return False
    return True

def is_pal_with_half_list(word):
    word_list = list(str(word)) # turn into string if it's a number
    # print(word_list)
    word_len = len(word_list)
    # print('word_len', word_len)
    if  word_len <= 1:
        return True
    for i in range(word_len // 2):
        # print(f'i: {i}, word_list[i]: {word_list[i]}, (word_len - i - 1): {word_len - i - 1}, word_list[word_len - i - 1]: {word_list[word_len - i - 1]}')
        if word_list[i] != word_list[word_len - i - 1]:
            return False
    return True

if __name__ == '__main__':

    # num = 119
    # p_num = get_next_pal(num, is_pal_with_reverse)
    # print(f'Started at {num} and found {p_num}')

    # num = 119
    # p_num = get_next_pal(num, is_pal_with_deque)
    # print(f'Started at {num} and found {p_num}')

    # num = '537373a'
    num = 537373
    p_num = get_next_pal(num, is_pal_with_half_list)
    if p_num:
        print(f'Started at {num} and found {p_num}')
    else:
        print('Please use a number')

