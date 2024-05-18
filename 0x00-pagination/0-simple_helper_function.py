#!/usr/bin/env python3
"""Task 0 Module"""


def index_range(page, page_size):
    """
    Return a tuple of size two containing a start index and an end index

    :param page: The page number (1-indexed)
    :param page_size: The number of items per page
    :return: A tuple (start_index, end_index)
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index
