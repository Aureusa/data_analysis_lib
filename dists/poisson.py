class PoissonDistribution:
    def __init__(self, lam: float):
        """
        Initialize the Poisson distribution with a given lambda (rate parameter).
        
        :param lam: The rate parameter (lambda) of the Poisson distribution
        :type lam: float
        """
        if lam <= 0:
            raise ValueError("Lambda must be a positive number.")
        self.lam = lam

    def pmf(self, k: int) -> float:
        """
        Calculate the probability mass function (PMF) for a given number of events k.
        
        :param k: The number of events
        :type k: int
        :return: The probability of observing k events
        :rtype: float
        """
        raise NotImplementedError("PMF function is not implemented yet.")
    