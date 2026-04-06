'''
Implements basic statistics like mean, median, standard deviation, covariance matric, etc.
'''
import numpy as np

import validation.arr_ops as val_arr


@val_arr.validate_axis
def mean(arr: np.ndarray, axis: int = None):
    """
    Calculate the mean of an array.

    :param arr: Input array
    :type arr: np.ndarray
    :return: Mean of the array
    :rtype: float
    """
    raise NotImplementedError("Mean function is not implemented yet.")


@val_arr.validate_axis
def median(arr: np.ndarray, axis: int = None):
    """
    Calculate the median of an array.

    :param arr: Input array
    :type arr: np.ndarray
    :return: Median of the array
    :rtype: float
    """
    raise NotImplementedError("Median function is not implemented yet.")


@val_arr.validate_axis
def std(arr: np.ndarray, axis: int = None):
    """
    Calculate the standard deviation of an array.

    :param arr: Input array
    :type arr: np.ndarray
    :return: Standard deviation of the array
    :rtype: float
    """
    raise NotImplementedError("Standard deviation function is not implemented yet.")


@val_arr.validate_2d_array
def covariance_matrix(arr: np.ndarray):
    """
    Calculate the covariance matrix of an array.

    :param arr: Input array (2D)
    :type arr: np.ndarray
    :return: Covariance matrix of the array
    :rtype: np.ndarray
    """
    raise NotImplementedError("Covariance matrix function is not implemented yet.")
