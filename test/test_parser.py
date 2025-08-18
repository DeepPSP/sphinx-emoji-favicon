import random
import re

from emoji import EMOJI_DATA, LANGUAGES
from tqdm.auto import tqdm

from sphinx_emoji_favicon import (
    _defalut_twemoji_latest_version,
    _str2emoji,
    _str2emoji_lang,
    _to_code_point,
    _url_is_reachable,
    create_emoji_favicon_meta,
)


def test_create_emoji_favicon_meta():
    check_link_probability = 0.01
    for emoji_unicode, emoji_data in tqdm(EMOJI_DATA.items(), total=len(EMOJI_DATA)):
        if "status" in emoji_data and emoji_data["status"] > 2:
            continue
        if "E" in emoji_data and str(emoji_data["E"]) > _defalut_twemoji_latest_version:
            continue
        if len(emoji_unicode) > 2:
            continue
        emoji_favicon_meta = create_emoji_favicon_meta(emoji_unicode)
        for lang in LANGUAGES:
            if lang not in emoji_data:
                continue
            emoji_str = emoji_data[lang]
            # Only assert if the unicode for this language string matches the base unicode
            lang_unicode = _str2emoji_lang[lang].get(emoji_str, emoji_str)
            if lang_unicode != emoji_unicode:
                print(f"Language mismatch for {emoji_unicode} in {lang}: {lang_unicode} != {emoji_unicode}")
                continue
            new_emoji_favicon_meta = create_emoji_favicon_meta(emoji_str, lang)
            assert new_emoji_favicon_meta == emoji_favicon_meta, f"Unexpected mismatch for {emoji_str} in {lang}"
            if random.random() <= check_link_probability:
                link = re.search(r'href="([^"]+)"', emoji_favicon_meta).group(1)
                # Do not assert _url_is_reachable(link) because some emoji are not yet available in Twemoji
                if not _url_is_reachable(link):
                    print(emoji_unicode)
                    print(emoji_str)
                    print("status:", emoji_data["status"])
                    print("version:", emoji_data["E"])
        for emoji_alias in emoji_data.get("alias", []):
            # Only assert if this alias maps exactly to the same unicode as the base one
            if emoji_alias in _str2emoji:
                alias_unicode = _str2emoji[emoji_alias]
                if alias_unicode != emoji_unicode:
                    continue
                assert create_emoji_favicon_meta(emoji_alias) == emoji_favicon_meta, f"Unexpected mismatch for {emoji_alias}"


def test_to_code_point():
    for emoji_unicode, emoji_data in tqdm(EMOJI_DATA.items(), total=len(EMOJI_DATA)):
        assert re.match("^[0-9a-f\\-]+$", _to_code_point(emoji_unicode))
