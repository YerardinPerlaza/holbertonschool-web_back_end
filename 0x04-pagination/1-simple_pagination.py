#!/usr/bin/env python3
"""Module that returns the list of results for a given page"""
import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Simple helper function to pagination"""
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Gets the results per page of the given page"""
        assert type(page) == int and page > 0
        assert type(page_size) == int and page_size > 0
        page_list = []
        results = self.dataset()
        indexes = index_range(page, page_size)
        try:
            for i in range(indexes[0], indexes[1]):
                page_list.append(results[i])
        except IndexError:
            pass
        return page_list
