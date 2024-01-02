import time
import audio, display, buttons, others, led

display_device = display.Display()
quick_buttons = buttons.Button(quick_start=True)
leds = led.LED(quick_start=True)

def home_page():
    home_group = display.createDisplayGroup()
    display_device.showDisplayGroup(home_group)

    bg_bitmap = display.createBitmap(160, 128)
    bg_colour_palette = display.createColourPalette([others.convertRGBToHex([0, 255, 0])])
    bg_sprite = display.createSprite(bg_bitmap, bg_colour_palette)
    display_device.showSprite(home_group, bg_sprite)

    fg_bitmap = display.createBitmap(150, 118)
    fg_colour_palette = display.createColourPalette([others.convertRGBToHex([255, 255, 0])])
    fg_sprite = display.createSprite(fg_bitmap, fg_colour_palette, 5, 5)

    display_device.showSprite(home_group, fg_sprite)

    text_group = display.createDisplayGroup(7, 10, 1)
    text_colour = (0, 0, 255)
    text = "Main Menu"
    text_label = display.createTextSprite(text, text_colour)
    display_device.showSprite(text_group, text_label)
    text_2 = "W: Tic-Tac-Toe"
    text_label_2 = display.createTextSprite(text_2, text_colour, 0, 15)
    display_device.showSprite(text_group, text_label_2)
    text_3 = "A: Rock-Paper-Scissors"
    text_label_3 = display.createTextSprite(text_3, text_colour, 0, 25)
    display_device.showSprite(text_group, text_label_3)
    text_4 = "S: Sine Wave Sound"
    text_label_4 = display.createTextSprite(text_4, text_colour, 0, 35)
    display_device.showSprite(text_group, text_label_4)

    display_device.showSprite(home_group, text_group)

sleep_time = 0.896
# Main loop
while True:
    # Show home screen
    home_page()

    # Wait for key press
    key_press = False
    while key_press == False:
        # print(quick_buttons.getButtonStateChange())
        time.sleep(sleep_time)
        leds.on()
        time.sleep(sleep_time)
        leds.off()
