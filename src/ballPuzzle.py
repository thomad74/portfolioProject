#!/usr/bin/env python3
"""application.py A program to sort a tube of different color balls to correctly labeled tubes by color. """

__author__      = "Dillon Thoma"
__date__        = "15 November 2018"

import pygame
import turtle
import stack
import ball_puzzle_animate
#import math

def move_ball(tube1, tube2):
    """
    :param tube1: the tube that the ball starts in
    :param tube2: the tube that the ball ends in
    :return: new sorted tubes
    :pre-condition: tube1 and tube2 are stacks
    :post-condition: tube1 and tube2 are sorted better
    """
    stack.push(tube2, stack.pop(tube1))
    return tube1, tube2

def solve_puzzle(inpt_balls):
    """
    Takes a string of different colors of balls, puts them into a stack, and
    sorts them by using an algorithm.
    :param inpt_balls: string of different colors of balls
    :return: none
    :pre-condition: inpt_balls is a string that contains only RGB values
    :post-condition: stacks are sorted and animated
    """
    red_tube = stack.make_empty_stack()
    green_tube = stack.make_empty_stack()
    blue_tube = stack.make_empty_stack()
    #yellow_tube = stack.make_empty_stack()
    stack_list = [red_tube, green_tube, blue_tube, yellow_tube]
    steps = 0

    for char in inpt_balls:
        stack.push(red_tube, char)

    while not stack.is_empty(red_tube):
        ball_color = red_tube.top.value

        if ball_color == "R" or ball_color == "G":
            move_ball(red_tube, green_tube)

ball_puzzle_animate.animate_move(stack_list, 1, 0)
steps += 1
#else:
    #move_ball(green_tube, blue_tube)

ball_puzzle_animate.animate_move(stack_list, 1, 2)
step += 1

while not stack.is_empty(blue_tube):
    ball_color = blue_tube.top.value

    if ball_color == "B":
        break
    move_ball(blue_tube, green_tube)

ball_puzzle_animate.animate_move(stack_list, 2, 1)
steps += 1
print(steps)
print("Close the window to quit.")
ball_puzzle_animate.animate_finish()

def main(): #Takes user input and sorts all the balls in a stack to their corresponding tubes by color.
    inpt_balls = input("Order of balls? ")

ball_puzzle_animate.animate_init(inpt_balls)
solve_puzzle(inpt_balls)

if __name__ == '__main__':
    main()
