from collections import deque
from typing import List

def rotate_left_till_zero(nums: List[int]) -> List[int]:
    # initialize a new deque out of nums
    queue = deque(nums)
    # continue the loop till front of queue is 0
    while queue[0] != 0:
        # remove the front of the queue and add it to the end
        queue.append(queue.popleft())
    # create a list out of the queue
    return list(queue)