class GaussianDistribution:
    def __init__(self, mean: float, std_dev: float):
        self.mean = mean
        self.std_dev = std_dev

    def pdf(self, x: float) -> float:
        """
        Calculate the probability density function (PDF) of the Gaussian distribution at a given point x.
        
        :param x: The point at which to evaluate the PDF
        :return: The value of the PDF at point x
        :rtype: float
        """
        raise NotImplementedError("PDF function is not implemented yet.")

    def cdf(self, x: float) -> float:
        """
        Calculate the cumulative distribution function (CDF) of the Gaussian distribution at a given point x.
        
        :param x: The point at which to evaluate the CDF
        :return: The value of the CDF at point x
        :rtype: float
        """
        raise NotImplementedError("CDF function is not implemented yet.")
    