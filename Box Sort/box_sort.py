# Author: Ditrung Duong
# GitHub username: ditrungduong
# Date: 10/13/2022
# Description: Initate a box class with volume calculating function. Create selection sort for volume after calculation

class Box:
    """"Represent a box with length, width and height"""
    def __init__(self, length, width, height):
        """Initiate a box with length, width and heigth"""
        self._length = length
        self._width = width
        self._height = height

    def volume(self):
        """Return volume of the box"""
        return self._length * self._width * self._height

    def get_length(self):
        """Return length of the box"""
        return self._length

    def get_width(self):
        """Return width of the box"""
        return self._width

    def get_height(self):
        """Return height of the box"""
        return self._height

    def __str__(self):
        return str(self._length)

def box_sort(box_list):
    """
     Sorts a_list of box in ascending order
     """
    box_list_volume = []
    for box in range(len(box_list)):
        box_list_volume.append(box_list[box].volume())
    for index in range(1, len(box_list_volume)):
        value = box_list_volume[index]
        pos = index - 1
        while pos >= 0 and box_list_volume[pos] > value:
            box_list_volume[pos + 1] = box_list_volume[pos]
            pos -= 1
        box_list_volume[pos + 1] = value
    return box_list_volume
