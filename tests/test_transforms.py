"""lib/transforms.py のユニットテスト。PR 時に GitHub Actions（CI）で実行される。"""

import sys
from pathlib import Path

import pytest

sys.path.append(str(Path(__file__).resolve().parent.parent / "lib"))
from transforms import categorize_amount


@pytest.mark.parametrize(
    ("amount", "expected"),
    [
        (0, "small"),
        (999, "small"),
        (1_000, "medium"),
        (9_999, "medium"),
        (10_000, "large"),
        (89_000, "large"),
        (99_999, "large"),
        (100_000, "xlarge"),
        (250_000, "xlarge"),
    ],
)
def test_categorize_amount(amount, expected):
    assert categorize_amount(amount) == expected


def test_negative_amount_raises():
    with pytest.raises(ValueError):
        categorize_amount(-1)
