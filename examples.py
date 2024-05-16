############## DO NOT USE ##############
# These examples are using the v0.1.2 package.
from sprig_essentials.io import display, audio, buttons
from sprig_essentials.graphics import shapes, text

# Example code
backlight = startBacklight(board.GP17)
spi = createSPI(board.GP18, board.GP19, board.GP16)
display_bus = createDisplayBus(spi, board.GP20, board.GP22, board.GP26)
display = initDisplay(display_bus, 160, 128, rotation=270)
# Alternatively, can also use "backlight, spi, display_bus, display = quickStartDisplay()"

group_1 = createDisplayGroup()
showDisplayGroup(display, group_1)

bg_bitmap = createBitmap(160, 128)
bg_colour_palette = createColourPalette([[0, 1, 0]])
bg_sprite = createSprite(bg_bitmap, bg_colour_palette, 0, 0)
showSprite(group_1, bg_sprite)

fg_bitmap = createBitmap(150, 118)
fg_colour_palette = createColourPalette([[0.7, 0, 0.4]])
fg_sprite = createSprite(fg_bitmap, fg_colour_palette, 5, 5)
showSprite(group_1, fg_sprite)

text_group = createDisplayGroup(11, 64, 2)
text = "Hello, World!"
text_label = createTextSprite(text, [[1, 1, 0]])
showSprite(text_group, text_label)

showSprite(group_1, text_group)

i2s = createI2S(board.GP10, board.GP11, board.GP9)

while True:
    pass
