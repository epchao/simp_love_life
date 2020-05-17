import pygame, pygame_menu
from game import *

screen_width = 0
screen_height = 0
menu_width = 720
menu_height = 1280
fullscreen = 0

pygame.init()
display = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

def newGame():
    main()

font = pygame_menu.font.FONT_8BIT
pygame.display.set_caption('Simp Love Life')
myTheme = pygame_menu.themes.Theme( widget_font=font,
                                    background_color = (0, 100, 200),
                                    title_shadow = True,
                                    title_bar_style = (pygame_menu.widgets.MENUBAR_STYLE_SIMPLE),
                                    title_font =font, 
                                    title_font_size = 54,
                                    widget_font_size = 54,
                                    )

menu = pygame_menu.Menu(menu_width, menu_height, 'SIMP LOVE LIFE', theme=myTheme)

menu.add_button('Play', newGame)
menu.add_button('Quit', pygame_menu.events.EXIT)
menu.mainloop(display)