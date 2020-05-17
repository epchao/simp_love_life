import pygame, pygame
import sys
import os
import menu
from res.libraries import ptext

# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

def main():
    # initialize
    pygame.init()
    display = menu.display
    background = pygame.Surface(display.get_size())
    background = background.convert()
    pygame.display.set_caption('Simp Love Life')
    clicked = False

    # fonts
    title_font = pygame.font.Font(os.path.abspath('res/fonts/8-bit.ttf'), 96)
    dialogue_font = pygame.font.Font(os.path.abspath('res/fonts/8-bit.ttf'), 48)
    choice_font = pygame.font.Font(os.path.abspath('res/fonts/8-bit.ttf'), 32)

    # title
    title = title_font.render("Simp Love Life", 1, WHITE)
    centerText(title, background, 0, 0)

    # classes
    class ClickableText(object):
        def __init__(self, text, position, size, color):
            self.image = pygame.Surface(size)
            self.image.fill(color)
            self.rect = pygame.Rect((0,0), size)

            text = choice_font.render(text, True, (WHITE))
            text_rect = text.get_rect()
            text_rect.center = self.rect.center

            self.image.blit(text, text_rect)

            self.rect.topleft = position

        def draw(self, screen):
            screen.blit(self.image, self.rect)

        def is_clicked(self, event):
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    return self.rect.collidepoint(event.pos)

    class Question:
        def __init__(self, stock_image_path, dialogue_text, choice_1, choice_2, choice_3=''):
            # parameters
            self.stock_image = pygame.image.load(stock_image_path).convert()
            self.stock_image_rect = self.stock_image.get_rect(center=display.get_rect().center)
            self.dialogue_text = dialogue_text
            self.choice_1 = choice_1
            self.choice_2 = choice_2
            self.choice_3_exists = False
            if choice_3 == '':
                pass
            else:
                self.choice_3_exists = True
                self.choice_3 = choice_3

        def render(self):
            display.blit(background, (0, 0))

            display.blit(self.stock_image, self.stock_image_rect.move(0, -200))

            ptext.draw(self.dialogue_text, (0, 600), fontname='res/fonts/8-bit.ttf', fontsize=38, align="center", color=WHITE)

            self.choice_1.draw(display)
            self.choice_2.draw(display)
            if self.choice_3_exists:
                self.choice_3.draw(display)
        
        def delete(self):
            display.fill(BLACK, (0, 70, 2000, 2000))

    q1 = Question('res/images/walkhome.png', """
                        One day, you are walking home late from sports practice and see a
                     friend of  yours. You pick up your pace and call out her name. “Hey Phoebe”. 
            She turns around and, in surprise, says “oh hey Marvin! 
            What are you doing walking home so late?""", 
            ClickableText("A.) I could say the same to you", (5, 750), (800, 50), BLACK),
            ClickableText("     B.) I was just coming home from practice", (50, 800), (800, 50), BLACK),
            ClickableText("C.) i was waiting for you!", (5, 850), (800, 50), BLACK))

    def mouseEvent(event, button):
        if button.is_clicked(event):
            clicked = True

    while True:
        for event in pygame.event.get():
            # quit game
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # esc menu
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            mouseEvent(event, q1.choice_1)
            mouseEvent(event, q1.choice_2)
            mouseEvent(event, q1.choice_3)

        q1.render()
        if clicked:
            display.fill(BLACK, (0, 750, 2000, 2000))
            clicked = False
        pygame.display.flip()
        pygame.display.update()

    

def centerText(text, bg, x, y):
    textpos = text.get_rect()
    textpos.centerx = bg.get_rect().centerx
    bg.blit(text, textpos.move(x, y))

if __name__ == '__main__':
    main()
