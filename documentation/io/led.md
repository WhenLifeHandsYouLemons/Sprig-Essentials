### `led` module

#### Initialisation

```py
import board
from sprig_essentials.io import led

# If you want to manually initialise the LED
led_device = led.LED(board.GP28)

# If you want to create the LED object and initialise it later
led_device = led.LED()

# If you are using this with a Sprig
led_device = led.LED(quick_start=True)
```

- **Parameters:**
  - `led_pin`: Pin number for the LED (default: `board.GP25`)
- **Returns:** `LED` object.

The `LED` class manages the Sprig's LED and its components. The initialisation functions in this class don't have to be called if you are using this with a Sprig.

---

#### `createLED`

Creates a digital output object for the specified pin.

- **Parameters:**
  - `led_pin`: Pin number for the LED
- **Returns:** `digitalio__digital_in_out` object.

Example:

```py
led_object = led.LED()
led_object.createLED(board.GP28)
```

---

#### `on`

Turns the LED on.

- **Parameters:** `None`
- **Returns:** `None`

Example:

```py
led_object = led.LED(board.GP28)
led_object.on()
```

---

#### `off`

Turns the LED off.

- **Parameters:** `None`
- **Returns:** `None`

Example:

```py
led_object = led.LED(board.GP28)
led_object.off()
```

---

#### `toggle`

Toggles the LED.

- **Parameters:** `None`
- **Returns:** `None`

Example:

```py
led_object = led.LED(board.GP28)
led_object.toggle()
```

---
