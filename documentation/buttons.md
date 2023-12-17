### `buttons` module

#### Initialisation

```py
import board
from sprig_essentials import button

# Initialize a button using a pin number
button_1 = button.Button(board.GP5)

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
button_object = button.createButton(board.GP5)
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
button = button.Button(board.GP5)
state = button.getPressed()    # Get state of specific button

# Or if using Sprig's 8 buttons
buttons = button.Button()
states = buttons.getPressed()    # Get state of all buttons
```

---

#### `updateButton`

Updates the current and previous state of the button.

- **Parameters:** `None`
- **Returns:** `None`.

Example:

```py
button = button.Button(board.GP5)
button.updateButton()    # Update state of specific button

# Or if using Sprig's 8 buttons
buttons = button.Button()
buttons.updateButton()    # Update state of all buttons
```

---

#### `getButtonStateChange`

Returns the state change of the button.

- **Parameters:** `None`
- **Returns:**:
  - `"pressed"` if state changes from `False` to `True`
  - `"released"` if state changes from `True` to `False`
  - `"no change"` if state did not change

Example:

```py
button = button.Button(board.GP5)
state_change = button.getButtonStateChange()    # Get state change of specific button

# Or if using Sprig's 8 buttons
buttons = button.Button()
state_changes = buttons.getButtonStateChange()    # Get state change of all buttons
```

---

#### `resetButtonStates`

Resets the current and previous state of the button.

- **Parameters:** `None`
- **Returns:** `None`.

Example:

```py
button = button.Button(board.GP5)
button.resetButtonStates()    # Reset state of specific button

# Or if using Sprig's 8 buttons
buttons = button.Button()
buttons.resetButtonStates()    # Reset state of all buttons
```

---
