def read_from_file():
    with open('input.txt', 'r') as file:
        return list(map(int, file.readline().split()))


def write_to_file(ans_list):
    with open('output.txt', 'w') as file:
        for item in ans_list:
            file.write(format(f"{item} "))


def solve_func(l):
    new_list = []
    for item in l:
        if not new_list.__contains__(item):
            new_list.append(item)
    return new_list


if __name__ == '__main__':
    write_to_file(solve_func(read_from_file()))

