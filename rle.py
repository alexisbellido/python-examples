# run-length encoding, also known as string compression
# turn aaaabbca into 4a2b1c1a

# see https://www.youtube.com/watch?v=mjZpZ_wcYFg

def f(n):
    if n <= 0:
        return 0
    return n + f(int(n/2))

if __name__ == '__main__':
    x = f(4)
    print(x)

