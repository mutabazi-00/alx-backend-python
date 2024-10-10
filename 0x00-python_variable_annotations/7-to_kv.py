#!/usr/bin/env python3
from typing import Union, Tuple
"""
This module provides a function that takes a string and a number, 
and returns a tuple where the number is squared and stored as a float.
"""

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple where the first element is a string and the second element is 
    the square of the number (int or float), returned as a float.

    Args:
        k (str): The input string.
        v (Union[int, float]): The input number to be squared.

    Returns:
        Tuple[str, float]: A tuple containing the string and the square of the number.
    """
    return (k, float(v ** 2))

