class BinomialDistribution:
    def __init__(self, n: int, p: float):
        self.n = n
        self.p = p

    def pmf(self, k: int) -> float:
        """
        Calculate the probability mass function for k successes.
        :param k: Number of successes
        :return: Probability of k successes
        :rtype: float
        """
        raise NotImplementedError("PMF function is not implemented yet.")

    def cdf(self, k: int) -> float:
        """
        Calculate the cumulative distribution function for k successes.
        :param k: Number of successes
        :return: Cumulative probability of k successes
        :rtype: float
        """
        raise NotImplementedError("CDF function is not implemented yet.")