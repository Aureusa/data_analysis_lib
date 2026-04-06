import numpy as np
from core import stats

def test_mean():
    data = np.array([1, 2, 3, 4, 5])
    result = stats.mean(data)
    expected = data.mean()
    assert np.isclose(result, expected), f"Expected {expected}, got {result}"

def test_median():
    data = np.array([1, 2, 3, 4, 5])
    result = stats.median(data)
    expected = np.median(data)
    assert np.isclose(result, expected), f"Expected {expected}, got {result}"

def test_std():
    data = np.array([1, 2, 3, 4, 5])
    result = stats.std(data)
    expected = data.std()
    assert np.isclose(result, expected), f"Expected {expected}, got {result}"

def test_covariance_matrix():
    data = np.array([[1, 2], [3, 4], [5, 6]])
    result = stats.covariance_matrix(data)
    expected = np.cov(data, rowvar=False)
    assert np.allclose(result, expected), f"Expected {expected}, got {result}"


if __name__ == "__main__":
    test_mean()
    test_median()
    test_std()
    test_covariance_matrix()
    print("All statistics tests passed!")