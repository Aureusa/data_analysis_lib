import numpy as np
from scipy.stats import norm


######################################
# Normal distribution tests
######################################


def test_gaussian_scalar():
    from dists import normal
    x = 0.5
    mu = 0.0
    sigma = 1.0
    result = normal.GaussianDistribution(mu, sigma).pdf(x)
    
    sp_result = norm.pdf(x, loc=mu, scale=sigma)
    assert np.isclose(result, sp_result), f"Expected {sp_result}, got {result}"

def test_gaussian_array():
    from dists import normal
    x = np.array([0.5, 1.0, 1.5])
    mu = 0.0
    sigma = 1.0
    result = normal.GaussianDistribution(mu, sigma).pdf(x)
    
    sp_result = norm.pdf(x, loc=mu, scale=sigma)
    assert np.allclose(result, sp_result), f"Expected {sp_result}, got {result}"

def test_gaussian_cdf_scalar():
    from dists import normal
    x = 0.5
    mu = 0.0
    sigma = 1.0
    result = normal.GaussianDistribution(mu, sigma).cdf(x)
    
    sp_result = norm.cdf(x, loc=mu, scale=sigma)
    assert np.isclose(result, sp_result), f"Expected {sp_result}, got {result}"

def test_gaussian_cdf_array():
    from dists import normal
    x = np.array([0.5, 1.0, 1.5])
    mu = 0.0
    sigma = 1.0
    result = normal.GaussianDistribution(mu, sigma).cdf(x)
    
    sp_result = norm.cdf(x, loc=mu, scale=sigma)
    assert np.allclose(result, sp_result), f"Expected {sp_result}, got {result}"


######################################
# Gamma distribution tests
######################################


def test_gamma_scalar():
    from dists import gamma
    x = 2.0
    shape = 2.0
    scale = 3.0
    result = gamma.GammaDistribution(shape, scale).pdf(x)
    
    from scipy.stats import gamma as sp_gamma
    sp_result = sp_gamma.pdf(x, a=shape, scale=scale)
    assert np.isclose(result, sp_result), f"Expected {sp_result}, got {result}"

def test_gamma_array():
    from dists import gamma
    x = np.array([1.0, 2.0, 3.0])
    shape = 2.0
    scale = 3.0
    result = gamma.GammaDistribution(shape, scale).pdf(x)
    
    from scipy.stats import gamma as sp_gamma
    sp_result = sp_gamma.pdf(x, a=shape, scale=scale)
    assert np.allclose(result, sp_result), f"Expected {sp_result}, got {result}"

def test_gamma_cdf_scalar():
    from dists import gamma
    x = 2.0
    shape = 2.0
    scale = 3.0
    result = gamma.GammaDistribution(shape, scale).cdf(x)
    
    from scipy.stats import gamma as sp_gamma
    sp_result = sp_gamma.cdf(x, a=shape, scale=scale)
    assert np.isclose(result, sp_result), f"Expected {sp_result}, got {result}"

def test_gamma_cdf_array():
    from dists import gamma
    x = np.array([1.0, 2.0, 3.0])
    shape = 2.0
    scale = 3.0
    result = gamma.GammaDistribution(shape, scale).cdf(x)
    
    from scipy.stats import gamma as sp_gamma
    sp_result = sp_gamma.cdf(x, a=shape, scale=scale)
    assert np.allclose(result, sp_result), f"Expected {sp_result}, got {result}"


######################################
# Poisson distribution tests
######################################


def test_poisson_scalar():
    from dists import poisson
    k = 3
    lam = 2.0
    result = poisson.PoissonDistribution(lam).pmf(k)
    
    from scipy.stats import poisson as sp_poisson
    sp_result = sp_poisson.pmf(k, mu=lam)
    assert np.isclose(result, sp_result), f"Expected {sp_result}, got {result}"

def test_poisson_array():
    from dists import poisson
    k = np.array([0, 1, 2, 3])
    lam = 2.0
    result = poisson.PoissonDistribution(lam).pmf(k)
    
    from scipy.stats import poisson as sp_poisson
    sp_result = sp_poisson.pmf(k, mu=lam)
    assert np.allclose(result, sp_result), f"Expected {sp_result}, got {result}"


######################################
# Binomial distribution tests
######################################

def test_binomial_scalar():
    from dists import binomial
    k = 5
    n = 10
    p = 0.5
    result = binomial.BinomialDistribution(n, p).pmf(k)
    
    from scipy.stats import binom as sp_binom
    sp_result = sp_binom.pmf(k, n=n, p=p)
    assert np.isclose(result, sp_result), f"Expected {sp_result}, got {result}"

def test_binomial_array():
    from dists import binomial
    k = np.array([0, 1, 2, 3, 4, 5])
    n = 10
    p = 0.5
    result = binomial.BinomialDistribution(n, p).pmf(k)
    
    from scipy.stats import binom as sp_binom
    sp_result = sp_binom.pmf(k, n=n, p=p)
    assert np.allclose(result, sp_result), f"Expected {sp_result}, got {result}"

def test_binomial_cdf_scalar():
    from dists import binomial
    k = 5
    n = 10
    p = 0.5
    result = binomial.BinomialDistribution(n, p).cdf(k)
    
    from scipy.stats import binom as sp_binom
    sp_result = sp_binom.cdf(k, n=n, p=p)
    assert np.isclose(result, sp_result), f"Expected {sp_result}, got {result}"

def test_binomial_cdf_array():
    from dists import binomial
    k = np.array([0, 1, 2, 3, 4, 5])
    n = 10
    p = 0.5
    result = binomial.BinomialDistribution(n, p).cdf(k)
    
    from scipy.stats import binom as sp_binom
    sp_result = sp_binom.cdf(k, n=n, p=p)
    assert np.allclose(result, sp_result), f"Expected {sp_result}, got {result}"

######################################
# Chi2 distribution tests
######################################

def test_chi2_scalar():
    from dists import chi2
    x = 2.0
    df = 3
    result = chi2.Chi2Distribution(df).pdf(x)
    
    from scipy.stats import chi2 as sp_chi2
    sp_result = sp_chi2.pdf(x, df=df)
    assert np.isclose(result, sp_result), f"Expected {sp_result}, got {result}"

def test_chi2_array():
    from dists import chi2
    x = np.array([1.0, 2.0, 3.0])
    df = 3
    result = chi2.Chi2Distribution(df).pdf(x)
    
    from scipy.stats import chi2 as sp_chi2
    sp_result = sp_chi2.pdf(x, df=df)
    assert np.allclose(result, sp_result), f"Expected {sp_result}, got {result}"

def test_chi2_cdf_scalar():
    from dists import chi2
    x = 2.0
    df = 3
    result = chi2.Chi2Distribution(df).cdf(x)
    
    from scipy.stats import chi2 as sp_chi2
    sp_result = sp_chi2.cdf(x, df=df)
    assert np.isclose(result, sp_result), f"Expected {sp_result}, got {result}"

def test_chi2_cdf_array():
    from dists import chi2
    x = np.array([1.0, 2.0, 3.0])
    df = 3
    result = chi2.Chi2Distribution(df).cdf(x)
    
    from scipy.stats import chi2 as sp_chi2
    sp_result = sp_chi2.cdf(x, df=df)
    assert np.allclose(result, sp_result), f"Expected {sp_result}, got {result}"

######################################
# F distribution tests
######################################

def test_f_scalar():
    from dists import f_anova as f
    x = 2.0
    dfn = 5
    dfd = 10
    result = f.FDistribution(dfn, dfd).pdf(x)
    
    from scipy.stats import f as sp_f
    sp_result = sp_f.pdf(x, dfn=dfn, dfd=dfd)
    assert np.isclose(result, sp_result), f"Expected {sp_result}, got {result}"

def test_f_array():
    from dists import f_anova as f
    x = np.array([1.0, 2.0, 3.0])
    dfn = 5
    dfd = 10
    result = f.FDistribution(dfn, dfd).pdf(x)
    
    from scipy.stats import f as sp_f
    sp_result = sp_f.pdf(x, dfn=dfn, dfd=dfd)
    assert np.allclose(result, sp_result), f"Expected {sp_result}, got {result}"

def test_f_cdf_scalar():
    from dists import f_anova as f
    x = 2.0
    dfn = 5
    dfd = 10
    result = f.FDistribution(dfn, dfd).cdf(x)
    
    from scipy.stats import f as sp_f
    sp_result = sp_f.cdf(x, dfn=dfn, dfd=dfd)
    assert np.isclose(result, sp_result), f"Expected {sp_result}, got {result}"

def test_f_cdf_array():
    from dists import f_anova as f
    x = np.array([1.0, 2.0, 3.0])
    dfn = 5
    dfd = 10
    result = f.FDistribution(dfn, dfd).cdf(x)
    
    from scipy.stats import f as sp_f
    sp_result = sp_f.cdf(x, dfn=dfn, dfd=dfd)
    assert np.allclose(result, sp_result), f"Expected {sp_result}, got {result}"


if __name__ == "__main__":
    # Gaussian distribution tests
    test_gaussian_scalar()
    test_gaussian_array()
    test_gaussian_cdf_scalar()
    test_gaussian_cdf_array()
    
    # Gamma distribution tests
    test_gamma_scalar()
    test_gamma_array()
    test_gamma_cdf_scalar()
    test_gamma_cdf_array()
    
    # Poisson distribution tests
    test_poisson_scalar()
    test_poisson_array()
    
    # Binomial distribution tests
    test_binomial_scalar()
    test_binomial_array()
    test_binomial_cdf_scalar()
    test_binomial_cdf_array()
    
    # Chi2 distribution tests
    test_chi2_scalar()
    test_chi2_array()
    test_chi2_cdf_scalar()
    test_chi2_cdf_array()

    # F distribution tests
    test_f_scalar()
    test_f_array()
    test_f_cdf_scalar()
    test_f_cdf_array()
    print("All distribution tests passed!")
