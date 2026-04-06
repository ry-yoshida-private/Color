"""
Smoke / integration tests for the color package.

From the repo root, with the package installed (``pip install -e .`` or deps from
``requirements.txt``):

  pytest tests/test.py -v

Without installing, point Python at ``src``:

  PYTHONPATH=src pytest tests/test.py -v

With unittest instead (same path layout; avoid a top-level package named ``test``):

  PYTHONPATH=src python3 -m unittest discover -s tests -p test.py -v
  PYTHONPATH=src python3 tests/test.py
"""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

import numpy as np

# Allow `python tests/test.py` without installing the package
_SRC = Path(__file__).resolve().parents[1] / "src"
if str(_SRC) not in sys.path:
    sys.path.insert(0, str(_SRC))

from color import (  # noqa: E402
    ColorConverter,
    ColorContainer,
    ColorFormat,
    ID2IntColor,
    Ratio2IntColor,
)
from color.container import Hex, HSV, RGB_FLOAT, RGB_INT, RGBA  # noqa: E402
from color.resolver import ColorFormatResolver  # noqa: E402


class TestColorConverter(unittest.TestCase):
    def test_rgb_int_hex_roundtrip(self) -> None:
        rgb = (255, 128, 0)
        hx = ColorConverter.RGB_INT2HEX(rgb)
        self.assertEqual(hx, "#ff8000")
        self.assertEqual(ColorConverter.HEX2RGB_INT(hx), rgb)

    def test_rgb_int_bgr_swap(self) -> None:
        rgb = (1, 2, 3)
        bgr = ColorConverter.RGB_INT2BGR_INT(rgb)
        self.assertEqual(bgr, (3, 2, 1))
        self.assertEqual(ColorConverter.BGR_INT2RGB_INT(bgr), rgb)

    def test_rgb_float_int(self) -> None:
        self.assertEqual(ColorConverter.RGB_FLOAT2RGB_INT((1.0, 0.0, 0.0)), (255, 0, 0))

    def test_gray(self) -> None:
        g = ColorConverter.RGB_INT2GRAY_INT((255, 255, 255))
        self.assertEqual(g, 255)
        self.assertAlmostEqual(ColorConverter.RGB_INT2GRAY_FLOAT((0, 0, 0)), 0.0)

    def test_hex_invalid_raises(self) -> None:
        with self.assertRaises(ValueError):
            ColorConverter.HEX2RGB_INT("#fff")


class TestRatio2IntColor(unittest.TestCase):
    def setUp(self) -> None:
        self.r2c = Ratio2IntColor()

    def test_bins(self) -> None:
        self.assertEqual(self.r2c.get_rgb_int_color(0.0), (139, 0, 0))
        self.assertEqual(self.r2c.get_rgb_int_color(0.05), (139, 0, 0))
        self.assertEqual(self.r2c.get_rgb_int_color(0.95), (0, 206, 209))
        self.assertEqual(self.r2c.get_rgb_int_color(1.0), (0, 206, 209))

    def test_bgr_matches_swap(self) -> None:
        r = 0.2
        rgb = self.r2c.get_rgb_int_color(r)
        bgr = self.r2c.get_bgr_int_color(r)
        self.assertEqual(bgr, ColorConverter.RGB_INT2BGR_INT(rgb))


class TestID2IntColor(unittest.TestCase):
    def test_stable_per_id(self) -> None:
        np.random.seed(0)
        m = ID2IntColor()
        c1 = m.get_rgb_int_color("a")
        c2 = m.get_rgb_int_color("a")
        self.assertEqual(c1, c2)
        np.random.seed(0)
        m2 = ID2IntColor()
        self.assertEqual(m2.get_rgb_int_color("a"), c1)

    def test_hex_and_bgr(self) -> None:
        np.random.seed(42)
        m = ID2IntColor()
        rgb = m.get_rgb_int_color("x")
        self.assertEqual(ColorConverter.HEX2RGB_INT(m.get_hex_color("x")), rgb)
        self.assertEqual(m.get_bgr_int_color("x"), ColorConverter.RGB_INT2BGR_INT(rgb))


class TestColorFormatResolver(unittest.TestCase):
    def test_tuple_shapes(self) -> None:
        self.assertEqual(ColorFormatResolver.resolve("#aabbcc"), ColorFormat.HEX)
        self.assertEqual(ColorFormatResolver.resolve((1, 2, 3)), ColorFormat.RGB_INT)
        self.assertEqual(ColorFormatResolver.resolve((1.0, 0.5, 0.0)), ColorFormat.RGB_FLOAT)
        self.assertEqual(ColorFormatResolver.resolve((1, 2, 3, 4)), ColorFormat.RGBA_INT)

    def test_ndarray(self) -> None:
        self.assertEqual(
            ColorFormatResolver.resolve(np.array([10, 20, 30], dtype=np.int32)),
            ColorFormat.RGB_INT,
        )
        self.assertEqual(
            ColorFormatResolver.resolve(np.array([0.1, 0.2, 0.3], dtype=np.float64)),
            ColorFormat.RGB_FLOAT,
        )
        self.assertEqual(
            ColorFormatResolver.resolve(np.array([1, 2, 3, 4], dtype=np.uint8)),
            ColorFormat.RGBA_INT,
        )

    def test_invalid(self) -> None:
        with self.assertRaises(ValueError):
            ColorFormatResolver.resolve((1, 2))
        with self.assertRaises(ValueError):
            ColorFormatResolver.resolve(np.zeros((2, 3)))


class TestColorContainerRegister(unittest.TestCase):
    def test_register_dispatches(self) -> None:
        h = ColorContainer.register("#00ff40")
        self.assertIsInstance(h, Hex)
        ri = ColorContainer.register((10, 20, 30))
        self.assertIsInstance(ri, RGB_INT)
        rf = ColorContainer.register((0.1, 0.2, 0.3))
        self.assertIsInstance(rf, RGB_FLOAT)
        ra = ColorContainer.register((1, 2, 3, 128))
        self.assertIsInstance(ra, RGBA)


class TestHexRgbRgbaFloat(unittest.TestCase):
    def test_hex_rgb_int_roundtrip(self) -> None:
        hx = Hex(value="#336699")
        ri = hx.to_rgb_int
        self.assertEqual((ri.r, ri.g, ri.b), (0x33, 0x66, 0x99))
        self.assertEqual(Hex.from_rgb_int(ri).value, "#336699")

    def test_rgb_float_hex(self) -> None:
        rf = RGB_FLOAT(value=(1.0, 0.0, 0.0))
        self.assertEqual(rf.to_hex.value, "#ff0000")

    def test_rgba_from_rgb_int(self) -> None:
        ri = RGB_INT(value=(100, 101, 102))
        ra = ri.to_rgba(alpha=10)
        self.assertEqual(ra.value, (100, 101, 102, 10))


class TestHSV(unittest.TestCase):
    def test_from_rgb_int_red(self) -> None:
        hsv = HSV.from_rgb_int(RGB_INT(value=(255, 0, 0)))
        # Pure red in colorsys: h=0, s=1, v=1
        self.assertAlmostEqual(hsv.h, 0.0, places=5)
        self.assertAlmostEqual(hsv.s, 1.0, places=5)
        self.assertAlmostEqual(hsv.v, 1.0, places=5)

    def test_roundtrip_approx(self) -> None:
        ri = RGB_INT(value=(12, 200, 90))
        hsv = HSV.from_rgb_int(ri)
        back = hsv.to_rgb_int
        self.assertEqual(back.r, ri.r)
        self.assertEqual(back.g, ri.g)
        self.assertEqual(back.b, ri.b)


if __name__ == "__main__":
    unittest.main()
