from collections import deque
from typing import Deque, List

def execute(program: List[str], queue: Deque[int]) -> Deque[int]:
    # initialize a deque representing a queue
    queue: Deque[int] = queue
    for instruction in program:
        if instruction == "peek":
            # print out the first item in queue if it is not empty
            # print warning message if queue is empty
            print(queue[0]) if queue else print("Queue is empty!")
        elif instruction == "pop":
            # check if queue is empty
            if queue:
                # pop the first item in queue
                queue.popleft()
            else:
                # print message if queue is empty
                print("Queue is empty!")
        else:
            if queue:
                print(instruction[5:])   
                # get the data in the "push" instruction
                data = int(instruction[5:])
                # push data to the end of queue
                queue.append(data)
            else:
                print("Queue is empty!")
    return queue