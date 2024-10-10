#!/usr/bin/env python3
from typing import Any, Sequence, Union

def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Returns the first element of the given sequence or None if the sequence is empty.

    Args:
        lst (Sequence[Any]): A sequence from which to retrieve the first element.

    Returns:
        Union[Any, None]: The first element of the sequence or None if the sequence is empty.
    """
    if lst:
        return lst[0]
    else:
        return None

