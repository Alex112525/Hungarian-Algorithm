def print_matrix(matrix):
    for row in matrix:
        print(row)
    print()


def neg_matrix(matrix):
    neg = [[(-1 * x) for x in row] for row in matrix]
    return neg


def max_matrix(matrix):
    maxim = [max(row) for row in matrix]
    return max(maxim)


def add_max(matrix, maxim):
    non_neg_matrix = [[(x + maxim) for x in row] for row in matrix]
    return non_neg_matrix


def sub_minima(matrix, opc="row"):
    min_matrix = []
    if opc == "row":        # Subtract row minima
        min_rows = [min(row) for row in matrix]
        min_matrix = [[(x - min_rows[i]) for x in row] for i, row in enumerate(matrix)]
    if opc == "col":        # Subtract column minima
        rot_matrix = [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix))]
        min_cols = [min(row) for row in rot_matrix]
        min_matrix = [[(x - min_cols[i]) for i, x in enumerate(row)] for row in matrix]
    return min_matrix


def find_zeros(matrix):
    rot_matrix = [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix))]
    row_zeros = [row.count(0) for row in matrix]
    col_zeros = [col.count(0) for col in rot_matrix]
    return row_zeros, col_zeros


def find_lines(matrix, h="row"):
    count = 0
    cpy_mat = [[ele for ele in row] for row in matrix]
    row_zeros, col_zeros = find_zeros(matrix) # [1, 2, 3 ,4 ]

    while max(row_zeros) and max(col_zeros):
        row_zeros, col_zeros = find_zeros(cpy_mat)
        if max(row_zeros) and max(col_zeros):
            if max(row_zeros) == max(col_zeros):
                if h == "row":
                    line = row_zeros.index(max(row_zeros))
                    opc = "row"
                else:
                    line = col_zeros.index(max(col_zeros))
                    opc = "col"
            elif max(row_zeros) > max(col_zeros):
                line = row_zeros.index(max(row_zeros))
                opc = "row"
            else:
                line = col_zeros.index(max(col_zeros))
                opc = "col"

            if opc == "row":
                for i in range(len(matrix)):
                    if cpy_mat[line][i] != "x":
                        cpy_mat[line][i] = "x"
                    else:
                        cpy_mat[line][i] = "t"
            else:
                for i in range(len(matrix)):
                    if cpy_mat[i][line] != "x":
                        cpy_mat[i][line] = "x"
                    else:
                        cpy_mat[i][line] = "t"
            count += 1
    return count, cpy_mat


def find_min_lines(matrix):
    n_lines_r, mark_matrix_r = find_lines(matrix, "row")    # 5
    n_lines_c, mark_matrix_c = find_lines(matrix, "col")    # 4
    if n_lines_r < n_lines_c:
        return n_lines_r, mark_matrix_r
    else:
        return n_lines_c, mark_matrix_c


def add_new_zeros(matrix, mark_mat):
    no_mark = []        #
    for row in mark_mat:
        for ele in row:
            if ele != "x" and ele != "t":
                no_mark.append(ele)

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if mark_mat[i][j] == "t":
                matrix[i][j] = matrix[i][j] + min(no_mark)
            if isinstance(mark_mat[i][j], int):
                matrix[i][j] = matrix[i][j] - min(no_mark)


def optimal_assignment(matrix):
    optimal = []
    n = 0
    index = 0
    while index < len(matrix):
        if 0 in matrix[index][n:]:
            op = matrix[index].index(0, n)
            if op not in optimal:
                optimal.append(op)
                index += 1
                n = 0
            else:
                n = op + 1
                if n > len(matrix)-1:
                    index -= 1
                    n = optimal[index] + 1
                    optimal.pop()
        else:
            index -= 1
            n = optimal.pop() + 1
    return optimal


def hungarian_Algorithm(matrix, opc="max"):
    if opc == "max":
        negate_matrix = neg_matrix(matrix)      # Negate all values
        max_value = max_matrix(matrix)
        non_neg_matrix = add_max(negate_matrix, max_value)  # Make the matrix non negative
        matrix = [[ele for ele in row] for row in non_neg_matrix]

    sub_min_rows = sub_minima(matrix)                   # Subtract row minima
    sub_min_cols = sub_minima(sub_min_rows, "col")      # Subtract column minima

    lines = 0
    print("Subtract column minima")
    print_matrix(sub_min_cols)
    while lines != len(matrix):
        lines, mark_matrix = find_min_lines(sub_min_cols)   # Cover all zeros with a minimum number of lines
        if lines < len(matrix):
            add_new_zeros(sub_min_cols, mark_matrix)        # Create additional zeros if the number of lines
            print_matrix(sub_min_cols)                      # is less than n (size of matrix)
    optimal_values = optimal_assignment(sub_min_cols)
    return optimal_values
