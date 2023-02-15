def read_matrix_from_file():
    with open('input.txt', 'r') as file:
        f = file.readlines()
        lst = [[float(n) for n in x.split()] for x in f]
        return lst


def write_matrix_to_file(matrix):
    f = open('output.txt', 'w')
    for x in range(len(matrix)):
        if x != 0:
            f.write('\n')
        for j in range(len(matrix[x])):
            f.write(str(matrix[x][j]) + ' ')
    f.close()


def find_indexes_where_min_and_max_el(matrix):
    min_el = matrix[0][0]
    max_el = matrix[0][0]
    min_index = 0
    max_index = len(matrix[0]) - 1
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] <= min_el:
                min_el = matrix[i][j]
                min_index = j
            if matrix[i][j] > max_el:
                max_el = matrix[i][j]
                max_index = j
            if matrix[i][j] == max_el:
                if j < max_index:
                    max_index = j
    return min_index, max_index


def solve_func(matrix):
    min_index, max_index = find_indexes_where_min_and_max_el(matrix)
    for i in range(len(matrix)):
        matrix[i][min_index], matrix[i][max_index] = matrix[i][max_index], matrix[i][min_index]
    return matrix


if __name__ == '__main__':
    matrix = read_matrix_from_file()
    write_matrix_to_file(solve_func(matrix))

