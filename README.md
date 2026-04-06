# Color

## Overview

Color (`color`) is a Python package for color utilities.
It provides color conversion helpers, ID-based color assignment, and ratio-to-color mapping.

For more details, see [src/color/README.md](src/color/README.md).

## Installation

From the package root (the directory containing `pyproject.toml`):

```bash
pip install .
```

For development, install in editable mode:

```bash
pip install -e .
```

Dependencies are installed automatically.

## Example

After installing the package, import it from any directory:

```python
from color import ColorConverter, ID2IntColor, Ratio2IntColor

rgb = (255, 128, 0)
hex_color = ColorConverter.RGB_INT2HEX(rgb)

id_mapper = ID2IntColor()
track_color = id_mapper.get_bgr_int_color("track-001")

ratio_mapper = Ratio2IntColor()
score_color = ratio_mapper.get_rgb_int_color(0.72)
```
