#!/usr/bin/python3
"""
Lockboxes – canUnlockAll

This module implements a simple depth‑first search to determine whether all boxes
can be opened given that box 0 is initially unlocked.
"""

from __future__ import annotations


def canUnlockAll(boxes: list[list[int]]) -> bool:
    """
    Determine if every box in the collection can be opened starting from box 0.

    Parameters
    ----------
    boxes : list[list[int]]
        A list where each element `boxes[i]` contains the keys found inside box i.
        Keys are positive integers; a key equal to a box number opens that box.
        Keys referring to non‑existent boxes are ignored.

    Returns
    -------
    bool
        True if every box can be opened, False otherwise.
    """
    n = len(boxes)
    visited = set()

    def dfs(i: int) -> None:
        """Recursive depth‑first search from box i."""
        if i in visited:
            return
        visited.add(i)
        for key in boxes[i]:
            # Only consider keys that refer to a real box.
            if 0 <= key < n:
                dfs(key)

    dfs(0)  # Box 0 is unlocked at the start.

    return len(visited) == n


# If this file is executed directly, run a quick manual test.
if __name__ == "__main__":
    boxes = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes))  # Expected: True

    boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes))  # Expected: True

    boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes))  # Expected: False
