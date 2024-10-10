#!/usr/bin/env python3
from typing import List, Union
"""
This module provides a function to sum a list of integers and floats.
"""

def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Returns the sum of a list containing integers and floats.

    Args:
        mxd_lst (List[Union[int, float]]): The list of integers and floats.

    Returns:
        float: The sum of the numbers in the list as a float.
    """
    return sum(mxd_lst)

