#!/usr/bin/python3

"""
Main script to test the 'canUnlockAll' function from 0-lockboxes module.
"""

from typing import List
from collections import deque

def canUnlockAll(boxes: List[List[int]]) -> bool:
    """
    Check if all boxes can be opened.

    Args:
        boxes (List[List[int]]): A list of lists containing keys to other boxes.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    n = len(boxes)
    visited = [False] * n
    queue = deque([0])  # Start with the first box

    while queue:
        current_box = queue.popleft()
        visited[current_box] = True

        for key in boxes[current_box]:
            if not visited[key]:
                queue.append(key)

    return all(visited)


if __name__ == "__main__":
    boxes1 = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes1))

    boxes2 = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes2))

    boxes3 = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes3))
