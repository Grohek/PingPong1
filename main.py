import pygame
import random

pygame.init()

# Screen window i gameloop
# Constants
paddle_speed = 10

screen = pygame.display.set_mode((560, 680))
pygame.display.set_caption("Ping Pong")
clock = pygame.time.Clock()

#paddle

paddle_width = 100
paddle_height = 10
player = pygame.Rect(240, 660, paddle_width, paddle_height)


#ball
ball_width = 10
ball_height = 10
ball = pygame.Rect(560 // 2 - ball_width // 2, 680 // 2 - ball_height // 2, 10, 10)
ball_speed_x = 5 * random.choice((1, -1))
ball_speed_y = 5 * random.choice((1, -1))

#
player_score = 0

font = pygame.font.Font(None, 36)
#gameloop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

#player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and player.left > 0:
        player.x -= paddle_speed
    if keys[pygame.K_d] and player.right < 560:
        player.x += paddle_speed

#ball movement
    ball.x += ball_speed_x
    ball.y += ball_speed_y

#ball collision with walls
    if ball.left <= 0 or ball.right >= 560:
        ball_speed_x *= -1
    if ball.top <= 0:
        ball_speed_y *= -1
#ball collision with player
    if ball.colliderect(player):
        ball_speed_y *= -1
        player_score += 1


    if ball.bottom >= 680:
        # Reset the ball position
        ball.x = 560 // 2 - ball_width // 2
        ball.y = 680 // 2 - ball_height // 2
        ball_speed_x *= random.choice((1, -1))
        ball_speed_y *= random.choice((1, -1))

        player_score -= 1

    clock.tick(60)

    screen.fill("white")

#player and ball draw
    pygame.draw.rect(screen, "orange", player)
    pygame.draw.ellipse(screen, "black", ball)
#score display
    score_text = font.render("Score: " + str(player_score), True, "black")
    screen.blit(score_text, (20,20))

    pygame.display.update()

pygame.quit()
