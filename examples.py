# pylint: disable=import-error, multiple-imports, too-few-public-methods, missing-class-docstring, invalid-name, multiple-statements, missing-function-docstring, missing-module-docstring, redefined-outer-name, line-too-long, consider-using-enumerate
import board
import displayio, digitalio, busio, terminalio, audiobusio, audiocore
from adafruit_display_text import label
from adafruit_st7735r import ST7735R
import array
import time
import math

# Reset all pins to allow new connections
displayio.release_displays()

# To show return tooltips for functions
class pin_number:pass
class digitalio__digital_in_out:pass
class busio__spi:pass
class displayio__display_bus:pass
class st7735r:pass
class displayio__group:pass
class displayio__bitmap:pass
class displayio__palette:pass
class displayio__sprite:pass
class terminalio__font:pass
class label__label:pass
class audiobusio__i2s:pass

# For displays
# Turn on backlight as it doesn't turn on automatically
def startBacklight(backlight_pin: pin_number) -> digitalio__digital_in_out:
    led = digitalio.DigitalInOut(backlight_pin)
    led.direction = digitalio.Direction.OUTPUT
    led.value = True
    return led

def createSPI(clock_pin: pin_number, MOSI_pin: pin_number, MISO_pin: pin_number) -> busio__spi:
    spi = busio.SPI(clock=clock_pin, MOSI=MOSI_pin, MISO=MISO_pin)
    return spi

def createDisplayBus(spi: busio__spi, cs_pin: pin_number, dc_pin: pin_number, reset_pin: pin_number) -> displayio__display_bus:
    display_bus = displayio.FourWire(spi, command=dc_pin, chip_select=cs_pin, reset=reset_pin)
    return display_bus

def initDisplay(display_bus: displayio__display_bus, width: int, height: int, rotation: int = 0, bgr: bool = True, auto_refresh: bool = True) -> st7735r:
    display = ST7735R(display_bus, width=width, height=height, rotation=rotation, bgr=bgr)
    display.auto_refresh = auto_refresh
    return display

# Automates display creation, assuming you're using a Sprig
def quickStartDisplay():
    backlight = startBacklight(board.GP17)
    spi = createSPI(board.GP18, board.GP19, board.GP16)
    display_bus = createDisplayBus(spi, board.GP20, board.GP22, board.GP26)
    display = initDisplay(display_bus, 160, 128, rotation=270)
    return backlight, spi, display_bus, display

# Similar to a div in HTML
def createDisplayGroup(x: int = 0, y: int = 0, scale: int = 1) -> displayio__group:
    group = displayio.Group(x=x, y=y, scale=scale)
    return group

def showDisplayGroup(display: st7735r, group: displayio__group):
    display.show(group)

def createBitmap(width: int, height: int, value_count: int = 1) -> displayio__bitmap:
    bitmap = displayio.Bitmap(width, height, value_count)
    return bitmap

def createColourPalette(colours: list) -> displayio__palette:
    color_palette = displayio.Palette(len(colours))
    for i in range(len(colours)):
        color_palette[i] = colours[i]
    return color_palette

def createSprite(bitmap: displayio__bitmap, pixel_shader: displayio__palette, x=0, y=0) -> displayio__sprite:
    sprite = displayio.TileGrid(bitmap, pixel_shader=pixel_shader, x=x, y=y)
    return sprite

def showSprite(group: displayio__group, sprite: displayio__sprite):
    group.append(sprite)

def createTextSprite(text: str, colour: list, font: terminalio__font = terminalio.FONT) -> label__label:
    text_area = label.Label(font, text=text, color=colour[-1])
    return text_area

def run_forever():
    while True:
        pass

# For audio
def createI2S(bit_clock_pin: pin_number, word_select_pin: pin_number, data_pin: pin_number) -> audiobusio__i2s:
    i2s = audiobusio.I2SOut(bit_clock_pin, word_select_pin, data_pin)
    return i2s

# Automates audio creation, assuming you're using a Sprig
def quickStartAudio():


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

run_forever()
