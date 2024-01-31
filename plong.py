import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 400
BALL_RADIUS = 10
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 60
FPS = 60

# Colors
WHITE = (0, 100, 255)
BLACK = (0, 0, 0)

# Initialize the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

# Clock to control the frame rate
clock = pygame.time.Clock()

# Paddle initialization
player_paddle = pygame.Rect(WIDTH - PADDLE_WIDTH - 10, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT*10)
opponent_paddle = pygame.Rect(10, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)

# Ball initialization
ball = pygame.Rect(WIDTH // 2 - BALL_RADIUS // 2, HEIGHT // 2 - BALL_RADIUS // 2, BALL_RADIUS, BALL_RADIUS)
ball_speed = [random.choice([1, -1]), random.choice([1, -1])]  # Random initial direction

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move paddles
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and opponent_paddle.top > 0:
        opponent_paddle.y -= 5
    if keys[pygame.K_DOWN] and opponent_paddle.bottom < HEIGHT:
        opponent_paddle.y += 5

    # Move the ball
    ball.x += ball_speed[0] * 10
    ball.y += ball_speed[1] * 5

    # Ball collision with paddles
    if ball.colliderect(player_paddle) or ball.colliderect(opponent_paddle):
        ball_speed[0] *= -1

    # Ball collision with top and bottom walls
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed[1] *= -1

    # Check for scoring
    if ball.left <= 0 or ball.right >= WIDTH:
        # Reset ball position
        ball.x = WIDTH // 2 - BALL_RADIUS // 2
        ball.y = HEIGHT // 2 - BALL_RADIUS // 2

        # Randomize ball direction
        ball_speed = [random.choice([1, -1]), random.choice([1, -1])]

    # Draw everything
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, player_paddle)
    pygame.draw.rect(screen, WHITE, opponent_paddle)
    pygame.draw.ellipse(screen, WHITE, ball)

    pygame.display.flip()
    clock.tick(FPS)

# Quit the game
pygame.quit()
