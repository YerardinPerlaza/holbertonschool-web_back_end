#!/usr/bin/env python3
"""Write a type-annotated function sum_mixed_list"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """takes mxd_lst of integers and floats and returns sum as a float"""
    total = 0
    for num in mxd_lst:
        total = total + num

    return total
