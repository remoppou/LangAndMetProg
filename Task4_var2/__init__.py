def read_from_file():
    with open('input.txt', 'r') as file:
        return file.readline()


def write_to_file(ans_list):
    with open('output.txt', 'w') as file:
        for item in ans_list:
            file.write(format(f"{item}\n"))


def solve_func(text):
    symbols = list(text)
    ans_list = []
    ch = ''
    bool_help = False
    for i in range(len(symbols)):
        if '0' <= symbols.__getitem__(i) <= '9':
            ch += symbols[i]
            continue
        if ch != '' and symbols.__getitem__(i) == '.' or symbols.__getitem__(i) == ',' and not bool_help:
            if i <= len(symbols) - 1:
                if '0' <= symbols.__getitem__(i + 1) <= '9':
                    ch += symbols[i]
                    bool_help = True
                    continue
        if ch != '':
            ans_list.append(ch)
            ch = ''
            bool_help = False
    return ans_list


if __name__ == '__main__':
    text = read_from_file()
    write_to_file(solve_func(text))
