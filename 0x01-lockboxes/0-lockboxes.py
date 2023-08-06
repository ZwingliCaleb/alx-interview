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
            if 0 <= key < n and not visited[key]:
                queue.append(key)

    return all(visited)


if __name__ == "__main__":
    boxes = [
        [7, 5],
        [1, 10, 7],
        [9, 6, 10],
        [7, 9],
        [2],
        [7, 3],
        [7, 9, 10, 10, 8, 9, 2, 5],
        [7, 2, 2, 4, 4, 2, 4, 8, 7],
        [4, 2, 9, 6, 6, 5, 5]
    ]

    try:
        result = canUnlockAll(boxes)
        print(result)
    except Exception as e:
        print(f"An error occurred: {e}")
