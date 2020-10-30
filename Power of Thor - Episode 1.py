import sys
import math

#   Problem: https://www.codingame.com/ide/puzzle/power-of-thor-episode-1
#   Author: Gracjan Redwanc s17393

# light_x: the X position of the light of power
# light_y: the Y position of the light of power
# initial_tx: Thor's starting X position
# initial_ty: Thor's starting Y position
light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]

current_position_x = initial_tx
current_position_y = initial_ty

while True:
    remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line.

    move_x = ""
    move_y = ""

    if light_y < current_position_y:
        move_y = "N"
        current_position_y -= 1
    if light_y > current_position_y:
        move_y = "S"
        current_position_y += 1
    if light_x > current_position_x:
        move_x = "E"
        current_position_x += 1
    if light_x < current_position_x:
        move_x = "W"
        current_position_x -= 1

    print(move_y + move_x)
