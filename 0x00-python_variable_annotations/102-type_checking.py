#!/usr/bin/env python3
from typing import Tuple, List

def zoom_array(lst: Tuple[int], factor: int = 2) -> List[int]:
    """
    Creates a new list where each element in `lst` is repeated `factor` times.

    Args:
        lst (Tuple[int]): The tuple of integers to zoom in on.
        factor (int): The number of times to repeat each element.

    Returns:
        List[int]: A new list with the elements of `lst` repeated `factor` times.
    """
    zoomed_in: List[int] = [
        item for item in lst
        for _ in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)  # Change to a tuple

zoom_2x = zoom_array(array)  # This is valid.

zoom_3x = zoom_array(array, 3)  # This is also valid.

