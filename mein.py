import pygame
from pygame import font

#COLORS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# make pygame do sumting
pygame.init()

# make window size
window = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("Catch")

# make image load in the thingy 
background = pygame.image.load("image.jpeg")
background = pygame.transform.scale(background, (1200, 800))

# make patrat !11!
rect1 = pygame.Rect(500, 150, 200, 75)  
rect2 = pygame.Rect(500, 500, 200, 75) 

# BE LIKE GOD WHEN HE CREATED LANGUAGE. -Actually humans created language- (idcccc it's my code )
font = pygame.font.Font(None, 32)  

# MAKE TEXT !!!!
text1 = font.render("1", True, BLACK)
text2 = font.render("2", True, BLACK)


print("\t__\n__")

# make frames!
clock = pygame.time.Clock()
FPS = 144
running = True
while running:
    # Clear the screen before drawing
    window.fill(BLACK)

    # show 
    window.blit(background, (0, 0))
    pygame.draw.rect(window, WHITE, rect1)
    pygame.draw.rect(window, WHITE, rect2)


    # make the text apeear on the rectzzz
    window.blit(text1, (rect1.x + rect1.width // 2 - text1.get_width() // 2, rect1.y + rect1.height // 2 - text1.get_height() // 2))
    window.blit(text2, (rect2.x + rect2.width // 2 - text2.get_width() // 2, rect2.y + rect2.height // 2 - text2.get_height() // 2))


    # make events work
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Check for mouse clicks
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if mouse is on rect
            if rect1.collidepoint(event.pos):
                print("!")
                screen_white = True  # Turn screen white on rect1 click
            elif rect2.collidepoint(event.pos):
                print("2!")
                screen_white = True  # Turn screen white on rect2 click

  

    # Update za display
    pygame.display.flip()
    clock.tick(FPS)

# Quit mothefucka!!
pygame.quit()
