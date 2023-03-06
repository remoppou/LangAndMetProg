import numpy


class Line:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c


class Intersection:

    def __init__(self, line1, line2):
        self.line1 = line1
        self.line2 = line2

    def __find_x_and_y(self):
        m = numpy.array([[self.line1.a, self.line1.b], [self.line2.a, self.line2.b]])
        v1 = - self.line1.c
        v2 = - self.line2.c
        v = numpy.array([v1, v2])
        return numpy.linalg.solve(m, v)

    def find_way(self):
        a = self.__find_x_and_y()
        x = a[0]
        y = a[1]
        return numpy.sqrt(x * x + y * y)


def read_lines_from_file():
    with open('input.txt', 'r') as file:
        f = file.readlines()
        ls = []
        lst = [[float(n) for n in x.split()] for x in f]
        for i in range(len(lst)):
            line = Line(lst[i][0], lst[i][1], lst[i][2])
            ls.append(line)
        return ls


def write_lines_to_file(inter):
    f = open('output.txt', 'w')
    f.write(format(f"{inter.line1.a, inter.line1.b, inter.line1.c}"))
    f.write('\n')
    f.write(format(f"{inter.line2.a, inter.line2.b, inter.line2.c}"))
    f.close()


def solve_method(ls):
    ans_ins = []
    way = 0
    for i in range(len(ls) - 1):
        k = i + 1
        for k in range(k, len(ls)):
            inter = Intersection(ls[i], ls[k])
            nw = inter.find_way()
            if i == 0 and k == 1:
                way = nw
                ans_ins = inter
            if nw < way:
                way = nw
                ans_ins = inter
    return ans_ins


if __name__ == '__main__':
    lines = read_lines_from_file()
    intersection = solve_method(lines)
    write_lines_to_file(intersection)
