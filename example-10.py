from datetime import datetime, date, time, timedelta

def get_input_file(path):
    lines = []
    with open(path) as file:
        for line in file:
            line = line.strip()
            lines.append(line)
    return lines


# >>> c1 = deque(['p3', 'p2', 'p1', 'p4', 'p1', 'p2', 'p5'])
# >>> c1
# deque(['p3', 'p2', 'p1', 'p4', 'p1', 'p2', 'p5'])
# >>> page = c1.popleft()
# >>> page
# 'p3'
# >>> c1
# deque(['p2', 'p1', 'p4', 'p1', 'p2', 'p5'])

def build_page_paths(lines):

    # C1 P3
    # C3 P2
    # C1 P1
    # C2 P3
    # C3 P2
    # C3 P2
    # C1 P2
    # C3 P2
    # C3 P3
    # C3 P3
    # C3 P2
    # C2 P3

    page_paths = {}

    for line in lines:
        data = line.split(',')
        user = data[1]
        page = data[2]
        print(user, page)
        if user in page_paths:
            page_paths[user].append(page)
        else:
            page_paths[user] = [page]

    return page_paths

def build_groups(pages):
    groups = []
    start = 0
    end = start + 3
    print('pages')
    print(pages)
    while start <= len(pages)-3:
        group = pages[start: end]
        groups.append(group)
    return groups

if __name__ == '__main__':

    path = 'input1.txt'
    # path = 'input2.txt'
    lines = get_input_file(path)

    page_paths = build_page_paths(lines)
    print(page_paths)
    # for user, pages in page_paths.items():
    #     print(user)
    #     print(pages)
    #     groups = build_groups(pages)
    #     print(groups)
    #     print('-------')
    #     break

