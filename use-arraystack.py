from arraystack import ArrayStack

if __name__ == '__main__':
    """
    A stack is a collection of objects that are inserted and removed according to
    he last-in, first-out (LIFO) principle.
    """
    # x = int(input("Enter a number\n"))
    print('Stack')
    S = ArrayStack()
    S.push(5)
    S.push(3)
    print(len(S))
    print(S.pop())
    print(S.is_empty())
    print(S.pop())
    print(S.is_empty())
    S.push(7)
    S.push(9)
    print(S.top())
    S.push(4)
    print(len(S))
    print('The stack contains', S.get())
    print('---------')

    print('Use ArrayStack to reverse file. Start with animals from bigger to smaller')
    animals_stack = ArrayStack()
    path = 'animals-by-size.txt'
    with open(path) as file:
        for line in file:
            animal = line.strip('\n')
            print('- ', animal)
            animals_stack.push(animal)

    print('Now pop stack to print animals from smaller to bigger')
    while not animals_stack.is_empty():
        print('- ', animals_stack.pop())
