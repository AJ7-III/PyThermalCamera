import io
import os
import sys
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from utils import is_raspberrypi


def test_is_raspberrypi_true(monkeypatch):
    def mock_open(*args, **kwargs):
        return io.StringIO("Raspberry Pi Model B")
    import utils
    monkeypatch.setattr(utils.io, 'open', mock_open)
    assert is_raspberrypi() is True


def test_is_raspberrypi_false(monkeypatch):
    def mock_open(*args, **kwargs):
        return io.StringIO("Some Other Device")
    import utils
    monkeypatch.setattr(utils.io, 'open', mock_open)
    assert is_raspberrypi() is False


def test_is_raspberrypi_missing(monkeypatch):
    def mock_open(*args, **kwargs):
        raise FileNotFoundError
    import utils
    monkeypatch.setattr(utils.io, 'open', mock_open)
    assert is_raspberrypi() is False
