class FDistribution:
    """
    Class representing the F-distribution, used in ANOVA tests.
    """
    def __init__(self, dfn: int, dfd: int):
        """
        Initialize the F-distribution with degrees of freedom for numerator and denominator.
        
        :param dfn: Degrees of freedom for the numerator
        :param dfd: Degrees of freedom for the denominator
        """
        self.dfn = dfn
        self.dfd = dfd
    
    def pdf(self, x: float) -> float:
        """
        Calculate the probability density function (PDF) of the F-distribution at a given value.
        
        :param x: Value at which to evaluate the PDF
        :return: PDF value at x
        """
        raise NotImplementedError("PDF function is not implemented yet.")
    
    def cdf(self, x: float) -> float:
        """
        Calculate the cumulative distribution function (CDF) of the F-distribution at a given value.
        
        :param x: Value at which to evaluate the CDF
        :return: CDF value at x
        """
        raise NotImplementedError("CDF function is not implemented yet.")
    