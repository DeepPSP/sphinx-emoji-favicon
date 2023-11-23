from emoji import EMOJI_DATA, LANGUAGES
from tqdm.auto import tqdm

from sphinx_emoji_favicon import _str2emoji, create_emoji_favicon_meta


def test_create_emoji_favicon_meta():
    for emoji_unicode, emoji_data in tqdm(EMOJI_DATA.items(), total=len(EMOJI_DATA)):
        emoji_favicon_meta = create_emoji_favicon_meta(emoji_unicode)
        for lang in LANGUAGES:
            if lang not in emoji_data:
                continue
            emoji_str = emoji_data[lang]
            assert create_emoji_favicon_meta(emoji_str, lang) == emoji_favicon_meta
        for emoji_alias in emoji_data.get("alias", []):
            if emoji_alias in _str2emoji:
                continue
            assert create_emoji_favicon_meta(emoji_alias) == emoji_favicon_meta
