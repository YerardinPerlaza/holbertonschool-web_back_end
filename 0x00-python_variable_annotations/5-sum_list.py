#!/usr/bin/env python3
"""Write a type-annotated function sum_list"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """takes a input_list of floats and returns their sum as a float."""
    total = 0
    for num in input_list:
        total = total + num

    return total
