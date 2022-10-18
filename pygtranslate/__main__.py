#!/usr/bin/env python3
import sys

from pygtranslate import translate

if __name__ == "__main__":

    print(translate(*sys.argv[1:]))
