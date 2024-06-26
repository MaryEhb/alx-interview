#!/usr/bin/python3
'''0. Lockboxes'''


def canUnlockAll(boxes):
    '''method that determines if all the boxes can be opened.'''
    if not isinstance(boxes, list) or len(boxes) == 0:
        return False
    openedSet = set()
    Unlock(boxes, openedSet, 0)
    return len(boxes) == len(openedSet)


def Unlock(boxes, openedSet, index):
    '''Recursively opens boxes and adds keys to the openedSet.'''
    if index not in openedSet:
        openedSet.add(index)
        for key in boxes[index]:
            if key < len(boxes):
                Unlock(boxes, openedSet, key)
