# Pygtranslate: Very Simple Python Google Translator

`pygtranslate` is an almost one line of code to translate language using Google translator.

## Requirement

- `python > 3.9`
- `requests`
- `lxml`

## How to use

You can translate any string with this module:

```python
>>> from pygtranslate import translate
>>> translate("I love you", "en", "de") # from en to de
"Ich liebe dich"
```

Or you can use cli:

```bash
python -m pygtranslate "I love you", "en", "de"
"Ich liebe dich"
```
