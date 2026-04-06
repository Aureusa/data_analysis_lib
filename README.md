# data_analysis_lib

# Structure of the library
```
data_analysis_lib/
│
├── core/
│   ├── stats.py        # mean, variance, covariance
│   ├── linalg.py       # matrix operations
|   ...
|
├── data/
│   ├── dataset.py      # pandas wrapper
|   ...
|
├── dists/
│   ├── normal.py
│   ├── gamma.py
│   ├── poisson.py
│   ├── binomial.py
│   ├── chi2.py
|   ...
|
├── models/
│   ├── linear_model.py # regression
│   ├── pca.py
|   ...
|
├── notebooks/
│   ├── notebook1.ipynb # for showcasing usage
|   ...
│
├── optimize/
│   ├── gradient_descent.py
|   ...
|
├── tests/ # Various test cases to ensure the library works as expected
│   ├── test_A.py
|   ├── test_B.py 
|   ...
|
├── validation/ Helpers for validating func args
│   ├── arr_ops.py # array validation
|   ...
│
├── viz/
│   ├── plotting.py     # matplotlib wrappers
```

# TODOs:

Phase 1: Core functionalities
- [ ] Implement basic statistical functions (mean, variance, std and covariance)
- [ ] Implement basic probability distributions (normal, gamma, poisson, binomial, chi-squared)
- [ ] Implement basic linear algebra operations (matrix multiplication, inversion, eigen decomposition)

Phase 2: TBD
