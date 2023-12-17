### Core module

#### Initialisation

Importing any other module from `sprig_essentials` will automatically initialise the core module.

---

#### `convertRGBToHex`

Converts an RGB value to a hex integer value.

Raises a `ValueError` if the RGB value is not between 0 and 255.
Raises a `TypeError` if the RGB value is not a list of integers.
Raises an `IndexError` if the RGB value is not a list of length 3.

- **Parameters:**
  - `rgb`: List of r, g, and b value.
- **Returns:** Hex integer value.

Example:

```py
hex_value = core.convertRGBToHex([255, 255, 255])
```

---
