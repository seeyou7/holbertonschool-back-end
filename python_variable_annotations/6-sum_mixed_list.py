#!/usr/bin/env python3
""" list of float & integer """
from typing import List, Union

def sum_mixed_list(mxd_lst: List[Union[float, int]]) -> float:
        """ Summation function for a list of floats and/or integers. """
        result: float = 0
        for number in mxd_lst:
            result+= number
        return result
