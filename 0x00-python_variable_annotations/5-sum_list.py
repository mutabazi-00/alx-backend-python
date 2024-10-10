#!/usr/bin/env python3
from typing import List
"""
This module provides a function to sum a list of floats.
"""

def sum_list(input_list: List[float]) -> float:
    """
    Returns the sum of a list of floats.

    Args:
        input_list (List[float]): The list of float numbers.

    Returns:
        float: The sum of the floats in the list.
    """
    return sum(input_list)

