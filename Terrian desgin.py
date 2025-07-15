import pygame
import sys
import os

pygame.init()

# Screen setup
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 512
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Player Jump with Vertical Barrier")

# Load and scale background
image_filename = "Rose-Hulman Funished background base.png"
if not os.path.exists(image_filename):
    print(f"Error: '{image_filename}' not found.")
    pygame.quit()
    sys.exit()

raw_bg = pygame.image.load(image_filename).convert()
bg_image = pygame.transform.scale(raw_bg, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Scroll variables
scroll_x = 0
scroll_speed = 4

# Player setup
player_width = 40
player_height = 60
player_x = 100
player_y_start = SCREEN_HEIGHT - player_height - 55
player_y = player_y_start
player_color = (200, 50, 50)
player_speed = 5

# Jump physics
gravity = 1
jump_power = -15
velocity_y = 0
is_jumping = False

# Ceiling = 1 player_speed above starting height
jump_ceiling = player_y_start - player_speed

clock = pygame.time.Clock()
running = True

while running:
    clock.tick(60)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Key detection
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player_x += player_speed
        scroll_x -= scroll_speed
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player_x -= player_speed
        scroll_x += scroll_speed

    # Jump
    if (keys[pygame.K_UP] or keys[pygame.K_w]) and not is_jumping:
        is_jumping = True
        velocity_y = jump_power

    # Apply gravity if jumping
    if is_jumping:
        player_y += velocity_y
        velocity_y += gravity

        # Stop upward movement at ceiling
        if player_y < jump_ceiling:
            player_y = jump_ceiling
            velocity_y = 0  # hit ceiling, stop going up

        # Land back on ground
        if player_y >= player_y_start:
            player_y = player_y_start
            is_jumping = False
            velocity_y = 0

    # Prevent off-screen horizontally
    if player_x < 0:
        player_x = 0
    if player_x + player_width > SCREEN_WIDTH:
        player_x = SCREEN_WIDTH - player_width

    # Scroll loop
    if scroll_x <= -SCREEN_WIDTH:
        scroll_x = 0
    if scroll_x >= SCREEN_WIDTH:
        scroll_x = 0

    # Draw background
    screen.blit(bg_image, (scroll_x, 0))
    screen.blit(bg_image, (scroll_x + SCREEN_WIDTH, 0))

    # Draw player
    pygame.draw.rect(screen, player_color, (player_x, player_y, player_width, player_height))

    # Update screen
    pygame.display.update()

pygame.quit()
sys.exit()

