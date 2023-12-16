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
