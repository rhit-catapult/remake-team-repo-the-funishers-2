import pygame
import sys
import os

# Initialize Pygame
pygame.init()

# Set screen size (your desired visible window size)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 512
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Scrolling Background - Scaled to Fit")

# Set image file name
image_filename = "Rose-Hulman Funished background base.png"

# Check if file exists
if not os.path.exists(image_filename):
    print(f"Error: '{image_filename}' not found.")
    pygame.quit()
    sys.exit()

# Load and scale background image to match screen size
raw_bg = pygame.image.load(image_filename).convert()
bg_image = pygame.transform.scale(raw_bg, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Scroll setup
scroll_x = 0
scroll_speed = 2

# Clock
clock = pygame.time.Clock()

# Main loop
running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Scroll background
    scroll_x -= scroll_speed
    if scroll_x <= -SCREEN_WIDTH:
        scroll_x = 0

    # Draw background loop
    screen.blit(bg_image, (scroll_x, 0))
    screen.blit(bg_image, (scroll_x + SCREEN_WIDTH, 0))

    pygame.display.update()

# Exit
pygame.quit()
sys.exit()
