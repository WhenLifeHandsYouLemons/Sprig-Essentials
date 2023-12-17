# sprig-essentials 0.3.1

Useful functions to simplify the process of creating games and apps with Sprig when using [CircuitPython](https://circuitpython.org/).

[![Upload Python Package](https://github.com/WhenLifeHandsYouLemons/sprig_essentials/actions/workflows/python-publish.yml/badge.svg)](https://github.com/WhenLifeHandsYouLemons/sprig_essentials/actions/workflows/python-publish.yml)

_**This package is not affiliated with Sprig or HackClub in any form.**_

---

## Installation

To install the correct CircuitPython firmware and libraries for the Raspberry Pi Pico, follow these steps:

1. Download the .UF2 from the CircuitPython website [here](https://circuitpython.org/board/raspberry_pi_pico/).
2. Press and hold the white button on the RPi Pico, then plug it into your computer while pressing the button. It should appear as a USB drive.
3. Drag the downloaded .UF2 file into the USB drive. The RPi Pico should automatically reboot and CircuitPython should be installed.
4. In the USB drive, create a new folder called `lib` if it doesn't already exist.
5. Download the necessary libraries from [this repository](https://github.com/WhenLifeHandsYouLemons/sprig-essentials/tree/cbcddaf0884fbc39bbaa791aa085280db103ce35/libraries) and place them in the `lib` folder.

To install `sprig_essentials` and use it on your Windows machine when developing for the Raspberry Pi Pico:

```txt
pip install sprig-essentials
```

This package is intended to run on the `Raspberry Pi Pico H`.

This package assumes you've installed `CircuitPython` and are using the `ST7735` display.

---

## Wiring Diagram

The wiring diagram that this package assumes is intended for anyone using a Sprig, however, you can also wire this manually and achieve the same effect.

![Image showing the pin connections from the Raspberry Pi Pico H to the various peripherals on the Sprig's board](https://camo.githubusercontent.com/d9b4afd8b99cc6befd3e04bdb8231c9fd134333ebd6a17166ca391429221ff05/68747470733a2f2f70617065722d6174746163686d656e74732e64726f70626f782e636f6d2f735f303531314241344231393135393837353345434243343935363743303632334234453646313535314241453338333243443842384232454441463236464142365f313636323537323037313339375f53637265656e2b53686f742b323032322d30392d30372b61742b312e33342e32312b504d2e706e67 "Taken from 'https://github.com/hackclub/sprig/blob/main/docs/GROWING_A_SPRIG.md'")

Here's a clearer electrical wiring diagram:

![Image showing the electric wiring diagram for the Raspberry Pi Pico H and the Sprig](https://camo.githubusercontent.com/f0ff037c476cfa07603e9c8ec77394ee53f18701c89f509a2852b623583d1807/68747470733a2f2f70617065722d6174746163686d656e74732e64726f70626f782e636f6d2f735f303531314241344231393135393837353345434243343935363743303632334234453646313535314241453338333243443842384232454441463236464142365f313636323537313738303737365f53637265656e2b53686f742b323032322d30392d30372b61742b312e31322e35372b504d2e706e67 "Taken from 'https://github.com/hackclub/sprig/blob/main/docs/GROWING_A_SPRIG.md'")

---

## Documentation

### `display` module

#### Initialisation

```py
import board
from sprig_essentials import display

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
  - `colours`: List of colours
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

### `Audio` module

#### Initialisation

```py
import board
from sprig_essentials import audio

audio_device = audio.Audio()
```

- **Parameters:**
  - `bit_clock_pin`: Pin number for the bit clock (default: `board.GP10`)
  - `word_select_pin`: Pin number for word select (default: `board.GP11`)
  - `data_pin`: Pin number for data (default: `board.GP9`)
- **Returns:** `Audio` object.

The `Audio` class manages audio output via the I2S interface. The initialization functions in this class don't have to be called if you are using this with a Sprig.

---

#### `createI2S`

Creates an I2S output object.

- **Parameters:**
  - `bit_clock_pin`: Pin number for the bit clock
  - `word_select_pin`: Pin number for word select
  - `data_pin`: Pin number for data
- **Returns:** `audiobusio__i2s` object.

Example:

```py
i2s_output = audio_device.createI2S(board.GP10, board.GP11, board.GP9)
```

---

#### `playWaveFile`

Plays a .wav file directly without additional lines.

- **Parameters:**
  - `wave_filename`: Filename of the .wav file
  - `loop`: Boolean for looped playback (default: `False`)
- **Returns:** `None`.

Example:

```py
audio_device.playWaveFile("example.wav", loop=True)
```

---

#### `playMP3File`

Plays an .mp3 file directly without additional lines.

- **Parameters:**
  - `mp3_filename`: Filename of the .mp3 file
  - `loop`: Boolean for looped playback (default: `False`)
- **Returns:** `None`.

Example:

```py
audio_device.playMP3File("example.mp3")
```

---

#### `playAudio`

Plays audio received from `createAudioSample` or `openWaveFile`.

- **Parameters:**
  - `audio`: Audio sample object (could be from [`createAudioSample`](#createaudiosample) or [`openWaveFile`](#openwavefile) or [`openMP3File`](#openmp3file))
  - `loop`: Boolean for looped playback (default: `False`)
- **Returns:** `None`.

Example:

```py
audio_device.playAudio(audio_sample, loop=True)
```

---

#### `isPlaying`

Checks if audio is currently playing.

- **Parameters:** `None`
- **Returns:** `bool`.

Example:

```py
playing = audio_device.isPlaying()
```

---

#### `stopAudio`

Stops all audio playback.

- **Parameters:** `None`
- **Returns:** `None`.

Example:

```py
audio_device.stopAudio()
```

---

#### `pauseAudio`

Pauses current audio playback.

- **Parameters:** `None`
- **Returns:** `None`.

Example:

```py
audio_device.pauseAudio()
```

---

#### `resumeAudio`

Resumes paused audio playback.

- **Parameters:** `None`
- **Returns:** `None`.

Example:

```py
audio_device.resumeAudio()
```

---

#### `createAudioSample`

Creates an audio sample from an input buffer for use with [`playAudio`](#playaudio).

- **Parameters:**
  - `audio_buffer`: [Input audio buffer](#createsinewave) (as `list` object with `int` values)
  - `sample_rate`: Sample rate (default: `8000`)
- **Returns:** `circuitpython_typing__AudioSample` object.

Example:

```py
audio_sample = createAudioSample(audio_buffer, sample_rate=16000)
```

---

#### `openWaveFile`

Opens 8-bit unsigned or 16-bit signed .wav files as samples.

- **Parameters:**
  - `wave_filename`: Filename of the .wav file
- **Returns:** `circuitpython_typing__AudioSample` object.

Example:

```py
wav_sample = openWaveFile("example.wav")
```

---

#### `openMP3File`

Opens .mp3 files as samples.

- **Parameters:**
  - `mp3_filename`: Filename of the .mp3 file
- **Returns:** `circuitpython_typing__AudioSample` object.

Example:

```py
mp3_sample = openMP3File("example.mp3")
```

---

#### `createSineWave`

Generates one period of a sine wave. Used as an example to show how an audio buffer can be created.

- **Parameters:** `None`
- **Returns:** `list[int]`.

Example:

```py
audio_buffer = createSineWave()
```

---

### `Button` class

#### Initialisation

```py
import board
from sprig_essentials import button

# Initialize a button using a pin number
button_1 = button.Button(board.GP4)

# Or if using a Sprig
buttons = button.Button(quick_start=True)
```

- **Parameters:**
  - `button_pin`: Pin number for the button (default: `None`)
  - `quick_start`: If `True`, initializes quick start buttons; if `False`, uses the specified `button_pin` (default: `False`)
- **Returns:** `Button` object.

The `Button` class manages button inputs on the Sprig. It allows the creation of buttons using specific pins or enables a quick start mode for predefined buttons.

---

#### `createButton`

Creates a digital input object for the specified pin.

- **Parameters:**
  - `btn_pin`: Pin number for the button
- **Returns:** `digitalio__digital_in_out` object.

Example:

```py
button = button.Button()
button_object = button.createButton(board.GP4)
```

---

#### `quickStartButtons`

Automates the creation of buttons assuming you're using a Sprig, providing quick start buttons.

- **Parameters:** `None`
- **Returns:** Tuple of digital input objects: `(w, a, s, d, i, j, k, l)`.

Example:

```py
button = button.Button()
quick_buttons = button.quickStartButtons()
```

---

#### `getPressed`

Gets the current state of the button.

- **Parameters:**
  - `button`: Optional digital input object; if provided, gets the state of this specific button
- **Returns:** If a specific button is provided, returns `True` if pressed, `False` if released. If no button is specified, returns a list of states for all buttons.

Example:

```py
button = button.Button(board.GP4)
state = button.getPressed()  # Get state of specific button
```

---

#### `updateButton`

Updates the current and previous state of the button.

- **Parameters:** `None`
- **Returns:** `None`.

This function is currently a placeholder for future implementation.

---

Enjoy creating, experimenting, and playing with a Sprig!

[Back to top ↑](#sprig_essentials-030)
