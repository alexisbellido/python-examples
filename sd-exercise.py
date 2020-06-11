from collections import deque


def get_next_pal(num, is_palindrome_fn):
    p_num = num + 1
    while not is_palindrome_fn(p_num):
        # print('current num', p_num)
        p_num += 1
    return p_num

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

if __name__ == '__main__':

    num = 119
    p_num = get_next_pal(num, is_pal_with_reverse)
    print(f'Started at {num} and found {p_num}')

    num = 119
    p_num = get_next_pal(num, is_pal_with_deque)
    print(f'Started at {num} and found {p_num}')
