#!/usr/bin/python3
""" A method that determines if all boxes can be opened or not."""

def canUnlockAll(boxes):
    """ Determines if the boxes can be opened.

    Args:
        boxes(list): a list of lists of boxes.
    Returns:
        True if all boxes can be opened, otherwise false."""
    if len(boxes) == 0:
        return False
    lockBoxes = len(boxes)
    boxUnlocked = [0]
    for i in boxUnlocked:
        for j in boxes[i]:
            if j not in boxUnlocked:
                if j < lockBoxes and lockBoxes != i:
                    boxUnlocked.append(j)
    if len(boxUnlocked) == lockBoxes:
        return True
    return False
