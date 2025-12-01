#!/usr/bin/python3
"""
Lockboxes – canUnlockAll

This module implements an iterative depth‑first search to determine whether all boxes
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
    stack = [0]          # start with the unlocked box 0

    while stack:
        i = stack.pop()
        if i in visited:
            continue
        visited.add(i)

        for key in boxes[i]:
            if 0 <= key < n and key not in visited:
                stack.append(key)

    return len(visited) == n


# Quick sanity check when run directly.
if __name__ == "__main__":
    # Example that triggers the recursion error previously
    boxes = [[j for j in range(1000)] for _ in range(1000)]
    print(canUnlockAll(boxes))          # Expected: True
