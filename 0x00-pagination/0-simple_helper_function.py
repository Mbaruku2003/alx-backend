#!/usr/bin/env python3
""" return a tuple of size two containing a start index and an end index."""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """corresponding to the range of indexes to return in a list."""

    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
