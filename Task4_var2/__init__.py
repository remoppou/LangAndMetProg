def read_from_file():
    with open('input.txt', 'r') as file:
        return file.readline()


def write_to_file(ans_list):
    s = len(ans_list) - 1
    with open('output.txt', 'w') as file:
        for item in ans_list:
            if s != 0:
                file.write(format(f"{item}\n"))
            else:
                file.write(format(f"{item}"))
            s -= 1


def solve_func(txt):
    symbols = list(txt)
    ans_list = []
    ch = ''
    is_point = False
    for i in range(len(symbols)):
        if '0' <= symbols[i] <= '9':
            ch += symbols[i]
            continue
        #Проверка на вещественное число
        if ch != '' and symbols[i] == '.' or symbols[i] == ',' and not is_point:
            if i <= len(symbols) - 1:
                if '0' <= symbols[i + 1] <= '9':
                    ch += symbols[i]
                    is_point = True
                    continue
        if ch != '':
            ans_list.append(ch)
            ch = ''
            is_point = False
    return ans_list


if __name__ == '__main__':
    text = read_from_file()
    write_to_file(solve_func(text))
