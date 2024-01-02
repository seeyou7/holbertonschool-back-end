#!/usr/bin/env python3
""" list of float"""
from typing import List


def sum_list(list: List[float]) -> float:
    """ Write anotation function """
    result: float = 0
    for i in list:
        result += i
    return result
