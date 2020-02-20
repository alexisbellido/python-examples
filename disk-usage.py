import os


def disk_usage(path):
    """
    Return the number of bytes used by a file or folder and its descendants.
    """
    total = os.path.getsize(path)
    if os.path.isdir(path):
        print(f"== {path} is a dir")
        for filename in os.listdir(path):
            childpath = os.path.join(path, filename)
            total += disk_usage(childpath)

    print('{0:<7}'.format(total), path)
    return total


if __name__ == '__main__':
    # path = input("Enter a path\n")
    path = '/root/project/static'
    disk_usage(path)
