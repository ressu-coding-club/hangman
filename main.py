import pygame
import math
import random

# setup game
pygame.init()
WIDHT, HEIGHT = 800, 500
win = pygame.display.set_mode((WIDHT, HEIGHT))
pygame.display.set_caption("Hangman")

# Button variables
RADIUS = 20
GAP = 15
letters = []
startx = round((WIDHT - (RADIUS * 2 + GAP) * 13) / 2)
starty = 400
A = 65
for i in range(26):
    x = startx + GAP * 2 + (RADIUS * 2 + GAP) * (i % 13)
    y = starty + ((i // 13) * (GAP + RADIUS * 2))
    letters.append([x, y, chr(A + i), True])

# Fonts
letter_font = pygame.font.SysFont("comicsans", 40)
word_font = pygame.font.SysFont("comicsans", 60)
tittle_font = pygame.font.SysFont("comicsans", 70)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# load images
images = []
for i in range(7):
    image = pygame.image.load("hangman" + str(i) + ".png")
    images.append(image)

# game variables
hangman_state = 0
words = ["DEVELOPER", "HELP", "PIZZA", "TRYHI"]
word = random.choice(words)
guessed = []

# setup game lopp
FPS = 60
clock = pygame.time.Clock()
run = True


def draw():
    win.fill(WHITE)
    # draw title
    text = tittle_font.render("Hangman", 1, BLACK)
    win.blit(text, (WIDHT / 2 - text.get_width() / 2, 20))
    # draw word
    display_word = ""
    for letter in word:
        if letter in guessed:
            display_word += letter + " "
        else:
            display_word += "_ "
    text = word_font.render(display_word, 1, BLACK)
    win.blit(text, (400, 200))

    # draw buttons
    for letter in letters:
        x, y, ltr, visible = letter
        if visible:
            pygame.draw.circle(win, BLACK, (x, y), RADIUS, 3)
            text = letter_font.render(ltr, 1, BLACK)
            win.blit(text, (x - text.get_width() / 2, y - text.get_height() / 2))

    win.blit(images[hangman_state], (150, 100))
    pygame.display.update()


def display_message(message):
    pygame.time.delay(1000)
    win.fill(WHITE)
    text = word_font.render(message, 1, BLACK)
    win.blit(text, (WIDHT / 2 - text.get_width() / 2, HEIGHT / 2 - text.get_height() / 2))
    pygame.display.update()
    pygame.time.delay(3000)


while run:
    clock.tick(FPS)
    draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            m_x, m_y = pygame.mouse.get_pos()
            for letter in letters:
                x, y, ltr, visible = letter
                if visible:
                    dis = math.sqrt((x - m_x) ** 2 + (y - m_y) ** 2)
                    if dis < RADIUS:
                        letter[3] = False
                        guessed.append(ltr)
                        if ltr not in word:
                            hangman_state += 1
    draw()

    won = True
    for letter in word:
        if letter not in guessed:
            won = False
            break
    if won:
        display_message("You Won!")
        break
    if hangman_state == 6:
        display_message("You Lost!")
        break

pygame.quit()

