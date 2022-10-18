#!/usr/bin/env python3
"""Translate string using Google translator"""
import requests
from lxml import html


def translate(
    target: str, from_lang: str = "auto", to_lang: str = "auto"
) -> str:
    """Returns the translation using google translate
    Please define `from_lang` and `to_lang` with iso code.
    (French = fr, English = en, Spanish = es, etc...)
    if not defined it will detect it or use english by default
    """
    link = (
        f"http://translate.google.com/m?tl={to_lang}&sl={from_lang}&q={target}"
    )

    return html.fromstring(requests.get(link).content).xpath(
        '//div[@class="result-container"]/text()'
    )[0]
