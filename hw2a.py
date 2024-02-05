from math import sqrt, pi, exp

def Probability(PDF, args, c, GT=True) :
    """
    This calculates the probability using simpson's 1/3 rule for a Gaussian/normal distribution.
    :param PDF: A callback function for the Gaussian/normal probability density function. This should
    take a single argument as a tuple, which contains values for x, mu (population mean) and sigma (population standard deviation).
    :param args: Is a tuple containing mu and sigma.
    :param c: Is the upper limit of integration.
    :param GT: A boolean indicating if we want the probability of x being greater than c (GT=True)
    or less than c (GT=False).
    :return: Probability value.
    """
    mu,sig=args
    if GT:
        a = mu - 5 * sig
        b = c
    else:
        a = c
        b = mu + 5 * sig
    def integrand(x):
        return PDF((x, mu, sig))
    Probability = Simpson13Rule(integrand, a, b, n=1000)
    return Probability

def Simpson13Rule(f, a, b, n):
    """
    :param f: Function to be integrated.
    :param a: Lower limit.
    :param b: Upper limit.
    :param n: Number of subintervals.
    :return: Integral Value
    """
    h = (b - a) / n
    x_values = [a + i * h for i in range(n + 1)]
    y_values = [f(x) for x in x_values]

    integral = y_values[0] + 4 * sum(y_values[1:n:2]) + 2 * sum(y_values[2:n-1:2]) + y_values[n]
    integral *= h / 3

    return integral
def GaussianPDF(x_mu_sigma):
    """
    This is the Guassian/Normal Probability Density Function.
    :param x_mu_sigma: Tuple containing values for x, mu and sigma.
    :return: PDF
    """
    x, mu, sigma = x_mu_sigma
    e = -0.5 * ((x - mu) / sigma) ** 2
    PDF = (1 / (sigma * sqrt(2 * pi))) * exp(e)
    return PDF
def main():
    # Result 1
    result1 = Probability(GaussianPDF, (100, 12.5), 105, GT=False)
    print(f'P(x<105|N(100,12.5))={result1:.2f}')
    #Result 2
    result2 = Probability(GaussianPDF, (100, 3), 100 + 2 * 3, GT=True)
    print(f'P(x>μ+2σ|N(100,3))={result2:.2f}')
if __name__ == "__main__":
    main()
