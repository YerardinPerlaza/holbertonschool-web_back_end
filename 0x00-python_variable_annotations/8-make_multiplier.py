#!/usr/bin/env python3
"""Write a type-annotated function make_multiplier"""
from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """takes a float multiplier as argument and returns a function"""
    def multiply_by(num: float) -> float:
        """that multiplies a float by multiplier"""
        return num * multiplier

    return multiply_by
    
