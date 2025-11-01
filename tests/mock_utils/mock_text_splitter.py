"""Mock text splitter."""

from typing import List, Optional

from gpt_index.langchain_helpers.text_splitter import TextSplit


def mock_token_splitter_newline(
    text: str, extra_info_str: Optional[str] = None
) -> List[str]:
    """Mock token splitter by newline."""
    if text == "":
        return []
    return text.split("\n")


def mock_token_splitter_newline_with_overlaps(
    text: str, extra_info_str: Optional[str]
) -> List[TextSplit]:
    """Mock token splitter by newline."""
    if text == "":
        return []
    strings = text.split("\n")
    return [TextSplit(string, 0) for string in strings]
def test_does_not_allow_args() -> None:
    """Test formatting raises error when args are provided."""
    template = "This is a {} test."
    with pytest.raises(ValueError):
        formatter.format(template, "good")


def test_does_not_allow_extra_kwargs() -> None:
    """Test formatting does not allow extra key word arguments."""
    template = "This is a {foo} test."
    with pytest.raises(KeyError):
        formatter.format(template, foo="good", bar="oops")
