# run-length encoding, also known as string compression
# turn aaaabbca into 4a2b1c1a

# see https://www.youtube.com/watch?v=mjZpZ_wcYFg

#  a  a  w  p  p  p  p  c  x

# prev = None
# cur = a
# char_list = a
# count 1
# count_list =
# prev a

# prev a
# cur a
# char_list a
# count 2
# count_list
# prev a

# cur w
# prev a
# char_list a w
# count_list 2
# count 1
# prev w

# cur p
# prev w
# char_list a w p
# count_list 2 1
# count 1
# prev p

# cur p
# prev p
# char_list a w p 
# count_list 2 1
# count 2
# prev  p

# cur p
# prev p
# char_list a w p
# count_list 2 1
# count 3
# prev p

###

# a w w

# cur a
# prev None
# char_list a
# count_list 
# count 1
# prev a

# cur w
# prev a
# char_list a w
# count_list 1
# count 1
# prev w

# cur w
# prev w
# char_list a w
# count_list 1 
# count 2
# prev w

# cur
# prev 
# char_list 
# count_list 
# count 
# prev 


def get_rle_1(text):
    prev = None
    count = 1
    encoded = ''
    char_list = []
    count_list = []
    for cur in text:
        if cur != prev:
            char_list.append(cur)
            if prev is not None:
                count_list.append(count)
                count = 1
        else:
            count += 1
        prev = cur
    count_list.append(count) # add count for final character
    # print(char_list)
    # print(count_list)
    for char, num in zip(char_list, count_list):
        # print(char, num)
        encoded += char + str(num)
    return encoded

def get_rle_2(text):
    prev = None
    count = 1
    encoded = []
    for cur in text:
        if cur == prev:
            count += 1
        else:
            if prev is not None:
                encoded.append(prev + str(count))
            count = 1
        prev = cur
    encoded.append(prev + str(count))
    return ''.join(encoded)

if __name__ == '__main__':

    text = 'aawppppcxx'
    print(text)
    encoded = get_rle_1(text)
    print('rle_1:', encoded)
    print('--')

    text = 'aawppppcxx'
    print(text)
    encoded = get_rle_2(text)
    print('rle_2:', encoded)
    print('--')
    
    # text = 'awp'
    # print(text)
    # encoded = get_rle_1(text)
    # print(encoded)
    # print('--')

    # text = 'XXXXX'
    # print(text)
    # encoded = get_rle_1(text)
    # print(encoded)
    # print('--')



