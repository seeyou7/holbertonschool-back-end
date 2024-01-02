#!/usr/bin/env python3
"""  type-annotated function to_kv that takes str int/float & return tuple """
from typing import Tuple, Union

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Convert a string and an integer/float to a tuple.

    Args:
    k (str): The string to be included in the tuple.
    v (Union[int, float]): An integer or float whose square will be the second element of the tuple.

    Returns:
    Tuple[str, float]: A tuple where the first element is the string k, 
                       and the second element is the square of v as a float.
    Convert v to float and square it, then return the tuple (k, v^2)
    """
    return (k, float(v) ** 2)
