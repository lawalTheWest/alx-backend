#!/usr/bin/env python3
'''
    a function named index_range that:
        takes two integer arguments page and page_size.

    returns:
        a tuple of size two containing a start index and
        an end index corresponding to the range of indexes
        to return in a list for those particular
        pagination parameters.
'''

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    '''
        returns a tuple
    '''
    return ((page - 1) * page_size, page * page_size)
