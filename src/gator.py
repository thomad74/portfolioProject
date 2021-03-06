#!/usr/bin/env python3
"""application.py  Python Program that creates a pop-up window with
a gator swimming through a body of water. """

__author__ = "Dillon Thoma"
__date__ = "18 December 2018"

# MUST import these packages to run this program.
import curses
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN
from random import randint
import pygame

curses.initscr()
win = curses.newwin(20, 60, 0, 0)
win.keypad(1)
curses.noecho()
curses.curs_set(0)
win.border(0)
win.nodelay(1)

# Colors of background and gator, respectively.
BLUE = (0, 0, 255)
GREEN = (124, 252, 0)
RED = (255, 0, 0)

# Set the width and height of each segement of the gator.
segment_width = 21
segment_height = 21
# The space between each segment of the gator.
segment_margin = 4

# Set initial speed that the gator swims.
x_change = segment_width + segment_margin
y_change = 0

# Creates and prints initial gator and piece of food.
gator = [[4, 10], [4, 9], [4, 8]]
food = [10, 20]

win.addch(food[0], food[1], '*')


class Segment(pygame.sprite.Sprite):
    # Constructor
    def __init__(self, x, y):
        # Call the parent's constructor
        super().__init__()

# Set height & width of the gator segments, and choose the color as GREEN.
        self.image = pygame.Surface([segment_width, segment_height])
        self.image.fill(GREEN)

# Creates the gator's starting point as the top left corner of the screen.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

# Function to initialize the pygame library.
pygame.init()

# Creates a screen that is 1000x900 in size.
screen = pygame.display.set_mode([1000, 800])

# Title of pop-up window that game is played in.
pygame.display.set_caption('Go Gators!')

allspriteslist = pygame.sprite.Group()

# Create an initial gator.
gator_segments = []
for i in range(15):
    x = 250 - (segment_width + segment_margin) * i
    y = 30
    segment = Segment(x, y)
    gator_segments.append(segment)
    allspriteslist.add(segment)

clock = pygame.time.Clock()
done = False

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        # Speed of the gator, depending on which key you press.
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = (segment_width + segment_margin) * -1
                y_change = 0
            if event.key == pygame.K_RIGHT:
                x_change = (segment_width + segment_margin)
                y_change = 0
            if event.key == pygame.K_UP:
                x_change = 0
                y_change = (segment_height + segment_margin) * -1
            if event.key == pygame.K_DOWN:
                x_change = 0
                y_change = (segment_height + segment_margin)

    # Deletes the last segment of the gator.
    old_segment = gator_segments.pop()
    allspriteslist.remove(old_segment)

    # Determining the location of the new segment.
    x = gator_segments[0].rect.x + x_change
    y = gator_segments[0].rect.y + y_change
    segment = Segment(x, y)

    # Inserting the new segment into the list.
    gator_segments.insert(0, segment)
    allspriteslist.add(segment)

    # Uses the variable created at the beginning to create the screen color.
    screen.fill(BLUE)

    allspriteslist.draw(screen)  # Creates the screen with the gator on it.

    pygame.display.flip()  # Flips the screen.

    clock.tick(5)  # How fast the gator is.

if gator[0] in gator[1:]:
    screen.fill(RED)  # If gator runs into itself, screen turns red.
if gator[0] == food:  # If the gator eats the food on screen, it will grow.
    food = []
    score += 1
    while food == []:
        food = [randint(1, 18), randint(1, 58)]
        if food in gator:
            food = []
    win.addch(food[0], food[1], '*')
else:  # If it does not eat, it will shrink and you will eventually lose.
    last = gator.pop()
    win.addch(last[0], last[1], ' ')
win.addch(gator[0][0], gator[0][1], '#')

pygame.quit()  # End of program gator.py.
