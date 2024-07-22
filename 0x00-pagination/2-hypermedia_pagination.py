#!/usr/bin/env python3

import csv
import math
from typing import List, Tuple, Dict, Any


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    '''
        Returns a tuple
    '''
    return ((page - 1) * page_size, page * page_size)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        '''
            retrieves index and return Page from REST API
        '''
        assert type(page) == int and page > 0
        assert type(page_size) == int and page_size > 0
        st_page, end_page = index_range(page, page_size)
        page_result = []
        if st_page >= len(self.dataset()):
            return page_result
        page_result = self.dataset()

        return page_result[st_page:end_page]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        '''
            Returns a dictionary.
        '''
        total_pages = math.ceil(len(self.dataset()) / page_size)
        return {
            "page_size": page_size,
            "page": page,
            "data": self.get_page(page, page_size),
            "next_page": page + 1 if page + 1 <= total_pages else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total_pages
        }
