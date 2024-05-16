### `display` module

#### Initialisation

```py
import board
from sprig_essentials.io import display

display_device = display.Display()
```

- **Parameters:**
  - `backlight_pin`: Pin number for the backlight (default: `board.GP17`)
  - `clock_pin`: Pin number for the clock (default: `board.GP18`)
  - `MOSI_pin`: Pin number for MOSI (default: `board.GP19`)
  - `MISO_pin`: Pin number for MISO (default: `board.GP16`)
  - `cs_pin`: Pin number for chip select (default: `board.GP20`)
  - `dc_pin`: Pin number for data/command (default: `board.GP22`)
  - `reset_pin`: Pin number for reset (default: `board.GP26`)
  - `screen_width`: Width of the screen (default: `160`)
  - `screen_height`: Height of the screen (default: `128`)
  - `rotation`: Display rotation in degrees (default: `270`)
  - `bgr`: Whether the display uses the BGR format or the RGB format (default: `True`)
  - `auto_refresh`: Whether auto-refresh is enabled (default: `True`)
- **Returns:** `display` object.

The `Display` class manages the Sprig's display device and its components.

The initialisation functions in this class don't have to be called if you are using this with a Sprig. If you're using a Sprig, chances are the wiring and parts are going to be the exact same for all boards, so you can initialise the screen using:

```py
screen = display.Display()
```

---

#### `startBacklight`

Turns on the backlight. You can also change the value of `display_device.backlight.value` to turn it on or off manually.

- **Parameters:**
  - `backlight_pin`: Pin number for the backlight
- **Returns:** `digitalio__digital_in_out` object.

Example:

```py
backlight = display_device.startBacklight(board.GP17)
```

---

#### `createSPI`

Creates an SPI object.

- **Parameters:**
  - `clock`: Clock pin
  - `mosi`: MOSI pin
  - `miso`: MISO pin
- **Returns:** `busio__spi` object.

Example:

```py
display_device_spi = display_device.createSPI(board.GP18, board.GP19, board.GP16)
```

---

#### `createDisplayBus`

Creates a display bus object.

- **Parameters:**
  - `spi`: [SPI object](#createspi)
  - `cs_pin`: Chip select pin
  - `dc_pin`: Data/command pin
  - `reset_pin`: Reset pin
- **Returns:** `displayio__display_bus` object.

Example:

```py
display_bus = display_device.createDisplayBus(spi, board.GP20, board.GP22, board.GP26)
```

---

#### `initDisplay`

Initializes the display object. Requires `self.display_bus` to be stored inside the class object already.

- **Parameters:**
  - `width`: Width of the display
  - `height`: Height of the display
  - `rotation`: Display rotation
  - `bgr`: Whether the display uses BGR
  - `auto_refresh`: Whether auto-refresh is enabled
- **Returns:** `st7735r` object.

Example:

```py
display = display_device.initDisplay(200, 100, 0, False, True)
```

---

#### `showDisplayGroup`

Shows a display group on the display.

- **Parameters:**
  - `group`: [Display group](#createdisplaygroup)
- **Returns:** `None`.

Example:

```py
display_device.showDisplayGroup(group)
```

---

#### `showSprite`

Shows a sprite on the display.

- **Parameters:**
  - `group`: [Display group](#createdisplaygroup)
  - `sprite`: [Sprite object](#createsprite)
- **Returns:** `None`.

Example:

```py
display_device.showSprite(group, sprite)
```

---

#### `createDisplayGroup`

Creates a display group.

- **Parameters:**
  - `x`: X-coordinate (default: `0`)
  - `y`: Y-coordinate (default: `0`)
  - `scale`: Scale factor (default: `1`)
- **Returns:** `displayio__group` object.

Example:

```py
group = createDisplayGroup()
```

---

#### `createBitmap`

Creates a bitmap object.

- **Parameters:**
  - `width`: Width of the bitmap
  - `height`: Height of the bitmap
  - `value_count`: Number of values (default: `1`)
- **Returns:** `displayio__bitmap` object.

Example:

```py
bitmap = createBitmap(10, 20)
```

---

#### `createColourPalette`

Creates a colour palette object.

- **Parameters:**
  - `colours`: Integer of a colour (use the [`convertRGBToHex` function](#convertrgbtohex) before inputting this value)
- **Returns:** `displayio__palette` object.

Example:

```py
colours = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]  # Example list of colours as a Tuple
palette = createColourPalette(colours)
```

---

#### `createSprite`

Creates a sprite.

- **Parameters:**
  - `bitmap`: [Bitmap](#createbitmap) for the sprite
  - `pixel_shader`: [Pixel shader](#createcolourpalette) for the sprite
  - `x`: X-coordinate (default: `0`)
  - `y`: Y-coordinate (default: `0`)
- **Returns:** `displayio__sprite` object.

Example:

```py
sprite = createSprite(bitmap, palette)
```

---

#### `createTextSprite`

Creates a text sprite.

- **Parameters:**
  - `text`: Text content for the sprite
  - `colour`: Colour for the text
  - `x`: X-coordinate (default: `0`)
  - `y`: Y-coordinate (default: `0`)
  - `font`: Font for the text (default: `terminalio.FONT`)
- **Returns:** `label__label` object.

Example:

```py
text_sprite = createTextSprite("Hello world!", (255, 0, 255))
```

---

#### `releaseDisplays`

Releases the display and display bus objects.

- **Parameters:** `None`.
- **Returns:** `None`.

Example:

```py
releaseDisplays()
```

---
