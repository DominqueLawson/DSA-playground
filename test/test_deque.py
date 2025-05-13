from data_structures.deque import execute
from typing import Deque

def test_deque():
    queue: Deque [int] = Deque([5, 4, 3, 45, 98, 1])
    assert execute(['peek', 'pop', 'push 8'], queue) == Deque([4, 3, 45, 98, 1, 8])