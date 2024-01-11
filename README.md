# Sphinx emoji favicon

[![PyPI](https://img.shields.io/pypi/v/sphinx-emoji-favicon?style=flat-square)](https://pypi.org/project/sphinx-emoji-favicon/)
[![codecov](https://codecov.io/github/DeepPSP/sphinx-emoji-favicon/graph/badge.svg?token=XO53nHzvUM)](https://codecov.io/github/DeepPSP/sphinx-emoji-favicon)
[![pytest](https://github.com/DeepPSP/sphinx-emoji-favicon/actions/workflows/run-pytest.yml/badge.svg)](https://github.com/DeepPSP/sphinx-emoji-favicon/actions/workflows/run-pytest.yml)
[![license](https://img.shields.io/github/license/DeepPSP/sphinx-emoji-favicon?style=flat-square)](LICENSE)
[![downloads](https://img.shields.io/pypi/dm/sphinx-emoji-favicon?style=flat-square)](https://pypistats.org/packages/sphinx-emoji-favicon)
![GitHub Release Date - Published_At](https://img.shields.io/github/release-date/DeepPSP/sphinx-emoji-favicon)
![GitHub commits since latest release (by SemVer including pre-releases)](https://img.shields.io/github/commits-since/DeepPSP/sphinx-emoji-favicon/latest)

A simple sphinx extension to add emoji favicon to your sphinx site.

This extension is inspired by [sphinx-favicon](https://github.com/tcmetzger/sphinx-favicon) and [streamlit](https://github.com/streamlit/streamlit).

Other related projects:

- [carpedm20/emoji](https://github.com/carpedm20/emoji)
- [twitter/twemoji](https://github.com/twitter/twemoji)

## Installation

```bash
pip install sphinx-emoji-favicon
```

## Usage

Add `sphinx_emoji_favicon` to your `conf.py`:

```python
extensions = [
    ...
    "sphinx_emoji_favicon",
    ...
]
```

Then add the following to your `conf.py`:

```python
emoji_favicon = "🦄"
# or emoji_favicon = ":unicorn:"
# or emoji_favicon = ":独角兽:"
```

or with additional options:

```python
emoji_favicon = {
    "emoji": ":lion:",  # "Leo" in English
    "language": "fr",
    "twemoji_cdns": "https://cdn.staticfile.org/twemoji/",  # or with version and/or assets type: "https://cdn.staticfile.org/twemoji/13.1.0/72x72/"
}
```
