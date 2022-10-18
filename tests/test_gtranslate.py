#!/usr/bin/env python3
from pygtranslate import translate


def test_translate() -> None:

    res = translate("I love you", "en", "de")
    assert res == "Ich liebe dich"
