#!/usr/bin/env python3
"""callable - functions"""

from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ 
    Creates and returns a multiplier function.

    This function, when called with a float 'multiplier', returns another function 'multiplier_func'.
    The returned function 'multiplier_func' will multiply any given float by the initial 'multiplier'.

    Args:
    multiplier (float): A float value which the returned function will use to multiply its input.

    Returns:
    Callable[[float], float]: A function that takes a float and returns the product of this float and the 'multiplier'.
    """

    def multiplier_func(number: float) -> float:
        """
        Multiplies the given number by a predetermined multiplier.

        Args:
        number (float): A float value to be multiplied by 'multiplier'.

        Returns:
        float: The result of multiplying 'number' by 'multiplier'.
        """
        return number * multiplier

    return multiplier_func
