from math import cos

def secant(fcn, x0, x1, maxiter=10, xtol=1e-5):
    """
    This uses the secant method to find the root of an equation.
    :param fcn: The function we want to find the root of.
    :param x0: First guess of the root.
    :param x1: Second guess of the root.
    :param maxiter: Maximum number of iterations.
    :param xtol: Tolerance
    :return: Final estimate of the root.
    """
    x_prev, x_curr = x0, x1
    for iteration in range(maxiter):
        f_prev = fcn(x_prev)
        f_curr = fcn(x_curr)
        if abs(f_curr - f_prev) < xtol:
            break
        x = x_curr - f_curr * (x_curr - x_prev) / (f_curr - f_prev)
        x_prev, x_curr = x_curr, x
    return x
def main():
    #Root 1
    root1 = secant(lambda x: x**2 - 3, 1, 2, maxiter=5, xtol=1e-4)
    print(f'Root guess (maxiter=5, xtol=1e-4): {root1:.4f}')
    #Root 2
    root2 = secant(lambda x: x**2 - 3, 1, 2, maxiter=15, xtol=1e-8)
    print(f'Root guess (maxiter=15, xtol=1e-8): {root1:.4f}')
    #Root 3
    root1 = secant(lambda x: x**2 - 3, 1, 2, maxiter=3, xtol=1e-8)
    print(f'Root guess (maxiter=3, xtol=1e-8): {root1:.4f}')
if __name__ == "__main__":
    main()