#!/usr/bin/python3
"""skd ak;js dalks d;al msdas"""


def find_peak(list_of_integers):
    """kjabnsdkjas ka"""
    largo = len(list_of_integers)
    if largo == 0:
        return None
    mid = largo // 2
    if (mid == largo - 1 or list_of_integers[mid] >= list_of_integers[mid + 1]) and (mid == 0 or list_of_integers[mid] >= list_of_integers[mid - 1]):
        return list_of_integers[mid]
    if mid != largo - 1 and list_of_integers[mid + 1] > list_of_integers[mid]:
        return find_peak(list_of_integers[mid + 1:])
    return find_peak(list_of_integers[:mid])
