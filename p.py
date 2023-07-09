import pygame
import time
import random

# Initialize Pygame
pygame.init()

# Set the width and height of the game window
width = 800
height = 600

# Set the colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# Create the game window
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')

# Set the game's clock
clock = pygame.time.Clock()

# Set the snake's initial position and speed
snake_position = [100, 50]
snake_segments = [[100, 50], [90, 50], [80, 50]]
direction = 'RIGHT'
change_to = direction
snake_speed = 10

# Set the food's initial position
food_position = [random.randrange(1, (width // 10)) * 10,
                 random.randrange(1, (height // 10)) * 10]
food_spawn = True

# Initialize the score
score = 0

# Define a function to display the score on the screen
def show_score(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score: ' + str(score), True, color)
    score_rect = score_surface.get_rect()
    if choice == 1:
        score_rect.midtop = (width / 10, 15)
    else:
        score_rect.midtop = (width / 2, height / 1.25)
    window.blit(score_surface, score_rect)


# Game Over function
def game_over():
    # Display the final score
    final_score = pygame.font.SysFont('arial', 35)
    score_surface = final_score.render('Your Score: ' + str(score), True, red)
    score_rect = score_surface.get_rect()
    score_rect.midtop = (width / 2, height / 4)
    window.blit(score_surface, score_rect)
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    quit()

# Main game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == ord('w'):
                change_to = 'UP'
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                change_to = 'RIGHT'

    # Validate the direction
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # Update snake position [x, y]
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10

    # Snake body mechanism
    snake_segments.insert(0, list(snake_position))
    if snake_position[0] == food_position[0] and snake_position[1] == food_position[1]:
        score += 1
        food_spawn = False
    else:
        snake_segments.pop()

    if not food_spawn:
        food_position = [random.randrange(1, (width // 10)) * 10,
                         random.randrange(1, (height // 10)) * 10]
    food_spawn = True

    # Window background color
    window.fill(black)

    # Draw the snake
    for segment in snake_segments:
        pygame.draw.rect(window, green, pygame.Rect(
            segment[0], segment[1], 10, 10))

    # Draw the food
    pygame.draw.rect(window, white, pygame.Rect(
        food_position[0], food_position[1], 10, 10))

    # Game Over conditions
    if snake_position[0] < 0 or snake_position[0] >= width or snake_position[1] < 0 or snake_position[1] >= height:
        game_over()
    for segment in snake_segments[1:]:
        if segment[0] == snake_position[0] and segment[1] == snake_position[1]:
            game_over()

    # Update the game display
    pygame.display.update()

    # Set the game's FPS
    clock.tick(snake_speed)
