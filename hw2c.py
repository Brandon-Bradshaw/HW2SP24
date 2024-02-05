def GaussSeidel(Aaug, x, Niter = 15):
    """
    This uses the Gauss-Seidel method to solve a system of equations.
    :param Aaug: Augmented matrix [A|B]
    :param x: Initial guess for the x vector.
    :param Niter: Number of iterations.
    :return: Vector x
    """
    N = len(x)
    # For the Diagonal Dominant Matrix
    for i in range(N):
        diagonal_element = abs(Aaug[i][i])
        row_sum = sum(abs(Aaug[i][j]) for j in range(N) if j != i)
    # Gauss-Seidel iterations
    for iteration in range(Niter):
        for i in range(N):
            sigma = sum(Aaug[i][j] * x[j] for j in range(N) if j != i)
            x[i] = (Aaug[i][N] - sigma) / Aaug[i][i]
        return x
    def main():
        # Matrix 1
        Aaug1 = [[3, 1, 1, 0],
                 [1, 4, 1, 0],
                 [2, 1, 2, 0]]
        x1 = [2, 12, 10]

        solution1 = GaussSeidel(Aaug1, x1)
        print(f'solution1: {solution1}')

        # Matrix 2
        Aaug2 = [[1, -10, 2, 4, 0],
                 [3, 1, 4, 12, 0],
                 [9, 2, 3, 4, 0],
                 [-1, 2, 7, 3, 0]]
        x2 = [2, 12, 21, 37]

        solution2 = GaussSeidel(Aaug2, x2)
        print(f'solution2: {solution2}')
    if __name__ == "__main__":
        main()
