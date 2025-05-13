from data_structures.hash_table import get_counter
from typing import Dict

def test_hash_table():
    assert get_counter([1, 2, 1, 3, 5, 5, 4, 3, 8, 9, 9]) == { 1: 2, 2: 1, 3: 2, 5: 2, 4: 1, 8: 1, 9: 2}