import pygame
import time

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Networked Pong")

# Initialize scores and font
p1_score = 0
p2_score = 0
game_over = False
font = pygame.font.Font(None, 60)
game_over_font = pygame.font.Font(None, 80)

player1_y = 250  # Initial position of the left paddle
player2_y = 250  # Initial position of the right paddle

#Ball variables
ball_x = 400  # Initial position of the ball
ball_y = 300  # Initial position of the ball
ball_dx = -5  # Horizontal velocity of the ball
ball_dy = 3  # Vertical velocity of the ball


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((20, 20, 30))  # Clear the screen with black
    if not game_over:
        keys = pygame.key.get_pressed()
        
            #player 1 controls
        if keys[pygame.K_w]:
            player1_y -= 5  # Move paddle up
        if keys[pygame.K_s]:
            player1_y += 5  # Move paddle down
        player1_y = max(0, min(player1_y, 500))  # Keep paddle within screen bounds
        
            #player 2 controls
        if keys[pygame.K_UP]:
            player2_y -= 5  # Move paddle up
        if keys[pygame.K_DOWN]:
            player2_y += 5  # Move paddle down
        player2_y = max(0, min(player2_y, 500))  # Keep paddle within screen bounds


        ball_x += ball_dx  # Update ball position
        ball_y += ball_dy  # Update ball position
        pygame.draw.circle(screen, (255, 255, 255), (ball_x, ball_y), 8)  # Ball

        #Wall collision detection
        if ball_y <= 8 or ball_y >= 592:
            ball_dy = -ball_dy
    
        #paddle collision detection
        if ball_x <= 78 and ball_x > 50 and ball_dx < 0:
            if player1_y - 8 <= ball_y <= player1_y + 108:
                ball_dx = -ball_dx
        
        if  ball_x >= 722 and ball_x < 750 and ball_dx > 0:
            if player2_y - 8 <= ball_y <= player2_y + 108:  # Check collision with right paddle
                ball_dx = -ball_dx
    
        if ball_x < -10:  # Ball goes out of bounds on the left side
            p2_score += 1
            time.sleep(0.5)  # Pause for a moment before resetting the ball
            ball_x, ball_y = 400, 300  # Reset ball position
            ball_dx = 5  # Reset ball direction
            ball_dy = 3
        elif ball_x > 810:  # Ball goes out of bounds on the right side
            p1_score += 1
            time.sleep(0.5)  # Pause for a moment before resetting the ball
            ball_x, ball_y = 400, 300  # Reset ball position
            ball_dx = -5  # Reset ball direction
            ball_dy = -3

        if p1_score >= 10 or p2_score >= 10:
                game_over = True  # End the game if a player reaches 10 points
        
    
    # Draw scores
    score1 = font.render(str(p1_score), True, (255, 255, 255))
    score2 = font.render(str(p2_score), True, (255, 255, 255))
    screen.blit(score1, (300, 30))
    screen.blit(score2, (480, 30))

    pygame.draw.rect(screen, (255, 255, 255), (50, player1_y, 20, 100))  # Left paddle
    pygame.draw.rect(screen, (255, 255, 255), (730, player2_y, 20, 100))  # Right paddle
    pygame.draw.line(screen, (255, 255, 255), (400, 0), (400, 600), 2)  # Center line

    if game_over:
            winner_text = "Player 1 Wins!" if p1_score >= 10 else "Player 2 Wins!"
            if winner_text == "Player 1 Wins!":
                game_over_surface = game_over_font.render(winner_text, True, (0, 255, 0))
                screen.blit(game_over_surface, (5, 500))
            else:
                game_over_surface = game_over_font.render(winner_text, True, (0, 255, 0))
                screen.blit(game_over_surface, (400, 500))

    pygame.display.flip()  # Update the display
    clock.tick(60)  # Limit the frame rate to 60 FPS

pygame.quit()