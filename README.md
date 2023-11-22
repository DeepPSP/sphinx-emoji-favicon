# Sphinx emoji favicon

[![PyPI](https://img.shields.io/pypi/v/sphinx-emoji-favicon?style=flat-square)](https://pypi.org/project/sphinx-emoji-favicon/)
[![license](https://img.shields.io/github/license/DeepPSP/sphinx-emoji-favicon?style=flat-square)](LICENSE)
[![downloads](https://img.shields.io/pypi/dm/sphinx-emoji-favicon?style=flat-square)](https://pypistats.org/packages/sphinx-emoji-favicon)

A simple sphinx extension to add emoji favicon to your sphinx site.

This extension is inspired by [sphinx-favicon](https://github.com/tcmetzger/sphinx-favicon) and [streamlit](https://github.com/streamlit/streamlit).


## Installation

```bash
pip install sphinx-emoji-favicon
```

## Usage

Add `sphinx_emoji_favicon` to your `conf.py`:

```python
extensions = [
    ...
    'sphinx_emoji_favicon',
    ...
]
```

Then add the following to your `conf.py`:

```python
emoji_favicon = '🦄'
# or emoji_favicon = ':unicorn:'
# or emoji_favicon = ':独角兽:'
```
