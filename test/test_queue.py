from data_structures.queue import rotate_left_till_zero

def test_queue():
    assert rotate_left_till_zero([4, 3, 10, 5, 0, 8, 9]) == [0, 8, 9, 4, 3, 10, 5]