import time
import board
from audio import *
from display import *

backlight = startBacklight(board.GP17)
spi = createSPI(board.GP18, board.GP19, board.GP16)
display_bus = createDisplayBus(spi, board.GP20, board.GP22, board.GP26)
display = initDisplay(display_bus, 160, 128, rotation=270)

def home_page():
    home_group = createDisplayGroup()
    showDisplayGroup(display, home_group)

    bg_bitmap = createBitmap(160, 128)
    bg_colour_palette = createColourPalette([convertRGBToHex([0, 255, 0])])
    bg_sprite = createSprite(bg_bitmap, bg_colour_palette, 0, 0)
    showSprite(home_group, bg_sprite)

    fg_bitmap = createBitmap(150, 118)
    fg_colour_palette = createColourPalette([convertRGBToHex([255, 255, 0])])
    fg_sprite = createSprite(fg_bitmap, fg_colour_palette, 5, 5)
    showSprite(home_group, fg_sprite)

    text_group = createDisplayGroup(7, 10, 1)
    text_colour = convertRGBToHex([0, 0, 255])
    text = "Main Menu"
    text_label = createTextSprite(text, [text_colour])
    showSprite(text_group, text_label)
    text_2 = "W: Tic-Tac-Toe"
    text_label_2 = createTextSprite(text_2, [text_colour], 0, 15)
    showSprite(text_group, text_label_2)
    text_3 = "A: Rock-Paper-Scissors"
    text_label_3 = createTextSprite(text_3, [text_colour], 0, 25)
    showSprite(text_group, text_label_3)
    text_4 = "S: Sine Wave Sound"
    text_label_4 = createTextSprite(text_4, [text_colour], 0, 35)
    showSprite(text_group, text_label_4)

    showSprite(home_group, text_group)


# Main loop
while True:
    # Show home screen
    home_page()

    # Wait for key press
    key_press = False
    while key_press == False:
        pass
