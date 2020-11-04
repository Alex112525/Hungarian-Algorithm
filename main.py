import Hungarian as Ha

if __name__ == "__main__":
    example1 = [[1, 2, 3],
                [2, 4, 6],
                [3, 6, 9]]

    example2 = [[3, 5, 5, 4, 1],
               [2, 2, 0, 2, 2],
               [2, 5, 4, 1, 0],
               [0, 1, 1, 1, 0],
               [1, 2, 1, 3, 3]]

    example3 = [[1, 2, 3, 4, 56, 32],
                [2, 4, 6, 23, 12, 87],
                [3, 6, 9, 32, 99, 12],
                [23, 45, 21, 73, 18, 51],
                [63, 98, 38, 19, 78, 43],
                [61, 93, 28, 33, 76, 19]]

    test = example1     # change example

    print("Input")
    Ha.print_matrix(test)

    if len(test) != len(test[0]):
        print("Ingrese una matriz cuadrada")
    else:
        Op_values = Ha.hungarian_Algorithm(test, "max")     # change if you want max or min

        Optimal_sum = 0
        for y, rows in enumerate(test):
            print(f"Optimal value {y+1}: {rows[Op_values[y]]}")
            Optimal_sum += rows[Op_values[y]]
        print("Suma de valores optimos:", Optimal_sum)
