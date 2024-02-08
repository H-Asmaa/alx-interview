#!/usr/bin/python3
def canUnlockAll(boxes):
    unlocked_boxes = {0}  # Start with box 0 unlocked
    prev_count = 0

    while len(unlocked_boxes) > prev_count:
        prev_count = len(unlocked_boxes)

        for box in unlocked_boxes.copy():
            unlocked_boxes.update(boxes[box])

    return len(unlocked_boxes) == len(boxes)

# Test cases
boxes1 = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes1))  # Should print True

boxes2 = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes2))  # Should print True

boxes3 = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes3))  # Should print False
