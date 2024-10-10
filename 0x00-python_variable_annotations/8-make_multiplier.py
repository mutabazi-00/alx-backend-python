#!/usr/bin/env python3
from typing import Callable
"""
This module provides a function that returns a function to multiply a float by a given multiplier.
"""

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by the given multiplier.

    Args:
        multiplier (float): The multiplier to apply.

    Returns:
        Callable[[float], float]: A function that takes a float and returns it multiplied by the multiplier.
    """
    def multiplier_func(n: float) -> float:
        """
        Multiplies the input float by the stored multiplier.

        Args:
            n (float): The number to multiply.

        Returns:
            float: The result of n multiplied by multiplier.
        """
        return n * multiplier

    return multiplier_func

