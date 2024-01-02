#!/usr/bin/env python3
"""
    type annotation ensures that the function's usage and 
    expectations are clear and can be checked 
    by static type checkers for correctness in terms of types
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Takes an iterable of sequences and returns a list of tuples,
    each containing a sequence from the iterable and its length.

    Args:
    lst (Iterable[Sequence]): An iterable containing sequences.

    Returns:
    List[Tuple[Sequence, int]]: A list of tuples where each tuple contains
                                a sequence and its length as an integer.
    """
    return [(i, len(i)) for i in lst]
