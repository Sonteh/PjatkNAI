import sys
import math

#   Problem: https://www.codingame.com/ide/puzzle/the-descent
#   Author: Gracjan Redwanc s17393

while True:
    mountain = 0
    highestMountain = 0

    for i in range(8):
        mountain_h = int(input())  # represents the height of one mountain.

        if mountain_h > highestMountain:
            highestMountain = mountain_h
            mountain = i

    print(mountain)
