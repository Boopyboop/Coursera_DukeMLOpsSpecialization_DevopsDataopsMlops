"""Pytest tests for hello.py functions."""

from hello import more_hello, more_goodbye

def test_more_hello():
    """Test greeting function."""
    assert more_hello() == "hi"

def test_more_goodbye():
    """Test farewell function."""
    assert more_goodbye() == "bye"
