#!/usr/bin/env python3
import csv
import math
from typing import List, Tuple


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """adding documentation for stuff that was provided to me..."""
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset adding documentation
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Returns a tuple of size two containing
    a start and end index corresponding to
    the range of the indexes to return in a
    list for those particular pagination params
    """
    start = (page - 1) * page_size
    end = start + page_size
    return start, end


    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """use index_range to find correct indexes to paginate
        the dataset corrrectly and return the appropriate page
        of the dataset (i.e. the correct list of rows)"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start, end = index_range(page, page_size)
        return self.dataset()[start:end]
