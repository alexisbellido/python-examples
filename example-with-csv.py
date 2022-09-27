from pprint import pprint
from datetime import datetime, date, time, timedelta
from csv import DictReader

def get_input_file(path):
    lines = []
    with open(path) as file:
        for line in file:
            line = line.strip()
            lines.append(line)
    return lines


def get_csv_file(path, fieldnames=None):
    rows = []
    with open(path, "r", encoding="utf-8") as csv:
        reader = DictReader(csv, fieldnames)
        for row in reader:
            rows.append(row)
    return rows

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

    path_txt = 'input1.txt'
    # path = 'input2.txt'
    lines = get_input_file(path_txt)

    # print(lines)
    pprint(lines)

    print("\n=================\n")
    
    # use first row as field names
    path_csv = 'input1.csv'
    rows = get_csv_file(path_csv)
    pprint(rows)
    # print(rows)

    print("\n=================\n")

    # pass field names
    path_csv = 'input1.txt'
    rows = get_csv_file(path_csv, fieldnames=['id', 'start', 'end', 'visits'])
    pprint(rows)
    # print(rows)

    # page_paths = build_page_paths(lines)
    # print(page_paths)
    # for user, pages in page_paths.items():
    #     print(user)
    #     print(pages)
    #     groups = build_groups(pages)
    #     print(groups)
    #     print('-------')
    #     break

