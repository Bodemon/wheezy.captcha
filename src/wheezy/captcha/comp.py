""" ``comp`` module.
"""

import sys

PY3 = sys.version_info[0] >= 3


if PY3:  # pragma: nocover
    from string import ascii_uppercase

    xrange = range
else:  # pragma: nocover
    from string import uppercase as ascii_uppercase  # noqa: F401

    xrange = xrange

try:  # pragma: nocover
    from PIL import Image, ImageFilter
    from PIL.ImageColor import getrgb
    from PIL.ImageDraw import Draw
    from PIL.ImageFont import truetype
except ImportError:  # pragma: nocover
    import Image  # noqa
    import ImageFilter  # noqa
    from ImageColor import getrgb  # noqa
    from ImageDraw import Draw  # noqa
    from ImageFont import truetype  # noqa
