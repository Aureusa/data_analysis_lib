class Chi2Distribution:
    def __init__(self, df: int):
        self.df = df

    def pdf(self, x: float) -> float:
        """
        Calculate the probability density function of the chi-squared distribution at a given value.

        :param x: Value at which to evaluate the PDF
        :type x: float
        :return: PDF value at x
        :rtype: float
        """
        raise NotImplementedError("PDF function is not implemented yet.")

    def cdf(self, x: float) -> float:
        """
        Calculate the cumulative distribution function of the chi-squared distribution at a given value.

        :param x: Value at which to evaluate the CDF
        :type x: float
        :return: CDF value at x
        :rtype: float
        """
        raise NotImplementedError("CDF function is not implemented yet.")
    