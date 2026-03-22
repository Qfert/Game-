import pygame
import random

pygame.init()
pygame.mixer.init()

WIDTH, HEIGHT = 1366, 768
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Square Clicker")

try:
    bg_image = pygame.image.load('background.png')
    bg_image = pygame.transform.scale(bg_image, (WIDTH, HEIGHT))
    pygame.mixer.music.load('music.mp3')
    pygame.mixer.music.play(-1) 
except:
    print("Файлы не найдены! Используем стандартный фон.")
    bg_image = None


SQUARE_SIZE = 50
square_color = (255, 0, 0) 
square_rect = pygame.Rect(random.randint(0, WIDTH-SQUARE_SIZE), 
                          random.randint(0, HEIGHT-SQUARE_SIZE), 
                          SQUARE_SIZE, SQUARE_SIZE)

score = 0
font = pygame.font.SysFont("Arial", 30)

running = True
while running:
    
    if bg_image:
        screen.blit(bg_image, (0, 0))
    else:
        screen.fill((20, 20, 20))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
      
        if event.type == pygame.MOUSEBUTTONDOWN:
            if square_rect.collidepoint(event.pos):
                score += 1
              
                square_rect.x = random.randint(0, WIDTH - SQUARE_SIZE)
                square_rect.y = random.randint(0, HEIGHT - SQUARE_SIZE)


    pygame.draw.rect(screen, square_color, square_rect)
    

    score_txt = font.render(f"Счет: {score}", True, (255, 255, 255))
    screen.blit(score_txt, (10, 10))

    pygame.display.flip()

pygame.quit()