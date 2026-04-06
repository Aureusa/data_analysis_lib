class GammaDistribution:
    """
    Class representing a Gamma distribution.
    """
    def __init__(self, shape: float, scale: float):
        self.shape = shape
        self.scale = scale
    
    def pdf(self, x: float) -> float:
        """
        Calculate the probability density function (PDF) of the Gamma distribution at a given point x.
        
        :param x: The point at which to evaluate the PDF
        :type x: float
        :return: The value of the PDF at point x
        :rtype: float
        """
        raise NotImplementedError("PDF function is not implemented yet.")
    
    def cdf(self, x: float) -> float:
        """
        Calculate the cumulative distribution function (CDF) of the Gamma distribution at a given point x.
        
        :param x: The point at which to evaluate the CDF
        :type x: float
        :return: The value of the CDF at point x
        :rtype: float
        """
        raise NotImplementedError("CDF function is not implemented yet.")
    