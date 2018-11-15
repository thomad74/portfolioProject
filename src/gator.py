#!/usr/bin/env python3
"""application.py  Python Program that creates a pop-up window with a gator swimming through a body of water. """

__author__      = "Dillon Thoma"
__date__        = "15 November 2018"

# MUST import the pygame package to run this program.
import pygame

# Colors of background and gator, respectively.
BLUE = (0, 0, 255)
GREEN = (124, 252, 0)

# Set the width and height of each segement of the gator.
segment_width = 21
segment_height = 21
# The space between each segment of the gator.
segment_margin = 4

# Set initial speed that the gator swims.
x_change = segment_width + segment_margin
y_change = 0

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
