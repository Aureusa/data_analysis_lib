import numpy as np
from functools import wraps


__all__ = ["validate_array", "validate_2d_array", "validate_non_empty_array", "validate_axis"]


def validate_array(func):
    @wraps(func)
    def wrapper(arr, *args, **kwargs):
        if not isinstance(arr, np.ndarray):
            raise TypeError(f"Input must be a numpy array, got {type(arr)} instead.")
        return func(arr, *args, **kwargs)
    return wrapper


def validate_2d_array(func):
    @wraps(func)
    def wrapper(arr, *args, **kwargs):
        if not isinstance(arr, np.ndarray):
            raise TypeError(f"Input must be a numpy array, got {type(arr)} instead.")
        if arr.ndim != 2:
            raise ValueError(f"Input array must be 2D, got {arr.ndim}D instead.")
        return func(arr, *args, **kwargs)
    return wrapper


def validate_non_empty_array(func):
    @wraps(func)
    def wrapper(arr, *args, **kwargs):
        if not isinstance(arr, np.ndarray):
            raise TypeError(f"Input must be a numpy array, got {type(arr)} instead.")
        if arr.size == 0:
            raise ValueError("Input array must be non-empty.")
        return func(arr, *args, **kwargs)
    return wrapper


def validate_axis(func):
    @wraps(func)
    def wrapper(arr, axis=None, *args, **kwargs):
        if not isinstance(arr, np.ndarray):
            raise TypeError(f"Input must be a numpy array, got {type(arr)} instead.")
        if axis is not None and (axis < 0 or axis >= arr.ndim):
            raise ValueError(f"Axis must be between 0 and {arr.ndim - 1}, got {axis} instead.")
        return func(arr, axis=axis, *args, **kwargs)
    return wrapper
