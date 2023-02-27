def read_matrix_from_file():
    with open('input.txt', 'r') as file:
        f = file.readlines()
        lst = [[int(n) for n in x.split()] for x in f]
        return lst


def write_matrix_to_file(mtx):
    f = open('output.txt', 'w')
    for x in range(len(mtx)):
        for j in range(len(mtx[x])):
            if j != len(mtx[x]) - 1:
                f.write(str(mtx[x][j]) + ' ')
            else:
                f.write(str(mtx[x][j]))
        f.write('\n')
    f.close()


def find_indexes_where_min_and_max_el(mtx):
    min_el = mtx[0][0]
    max_el = mtx[0][0]
    min_index = 0
    max_index = 0
    for i in range(len(mtx)):
        for j in range(len(mtx[i])):
            if mtx[i][j] <= min_el:
                min_el = mtx[i][j]
                min_index = j
            if mtx[i][j] > max_el:
                max_el = mtx[i][j]
                max_index = j
    return min_index, max_index


def solve_func(mtx):
    min_index, max_index = find_indexes_where_min_and_max_el(mtx)
    for i in range(len(mtx)):
        mtx[i][min_index], mtx[i][max_index] = mtx[i][max_index], mtx[i][min_index]
    return mtx


if __name__ == '__main__':
    mtx = read_matrix_from_file()
    write_matrix_to_file(solve_func(mtx))

