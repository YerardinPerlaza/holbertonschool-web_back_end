#!/usr/bin/env python3
"""Write a type-annotated function to_kv"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """takes a string k and an int OR float v as arguments and returns a tuple.
    The 1 element of the tuple is the string k.
    The 2 element is the square of v and should be annotated as a float."""
    tuple_kv = [k, v * v]
    return tuple_kv
