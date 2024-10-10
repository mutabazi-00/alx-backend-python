#!/usr/bin/env python3
from typing import Iterable, List, Sequence, Tuple

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples containing each element from the input list and its length.

    Args:
        lst (Iterable[Sequence]): An iterable containing sequences (e.g., strings, lists).

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples where each tuple contains an element and its length.
    """
    return [(i, len(i)) for i in lst]

