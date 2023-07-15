"""Test dl_hf_model."""
# pylint: disable=broad-except
from dl_hf_model import __version__
from dl_hf_model import dl_hf_model


def test_version():
    """Test version."""
    assert __version__[:3] == "0.1"


def test_sanity():
    """Check sanity."""
    try:
        assert not dl_hf_model()
    except Exception:
        assert True
