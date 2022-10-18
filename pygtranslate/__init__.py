#!/usr/bin/env python3
from typing import Any

from pygtranslate.core import translate

__all__ = ["translate"]


def main(argv: list[str]) -> str:

    return translate(argv[1], argv[2], argv[3])
