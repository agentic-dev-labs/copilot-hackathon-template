import json

import pytest

from app.config import load, slugify


def test_slug_is_azure_safe() -> None:
    assert slugify("Ali Farahnak") == "ali-farahnak"
    assert slugify("  Bill  Leeson ") == "bill-leeson"
    assert slugify("Jean-Luc O'Brien") == "jean-luc-o-brien"


def test_slug_stays_within_the_length_limit() -> None:
    slug = slugify("Christopher Papadopoulos Wellington the Third")
    assert len(slug) <= 32
    assert not slug.endswith("-")


def test_slug_must_start_with_a_letter() -> None:
    assert slugify("123 Numeric").startswith("a-")


def test_slug_rejects_a_name_with_no_usable_characters() -> None:
    with pytest.raises(ValueError):
        slugify("---")


def test_load_rejects_the_unedited_placeholder(tmp_path) -> None:
    config = tmp_path / "config.json"
    config.write_text(json.dumps({"displayName": "Your Name"}), encoding="utf-8")
    with pytest.raises(ValueError, match="replace 'Your Name'"):
        load(config)


def test_load_returns_display_and_app_names(tmp_path) -> None:
    config = tmp_path / "config.json"
    config.write_text(json.dumps({"displayName": "Team Zero"}), encoding="utf-8")
    assert load(config) == {"displayName": "Team Zero", "appName": "team-zero"}
