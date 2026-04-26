from seasons import validate
import pytest

def test_valid():
    with pytest.raises(SystemExit):
        validate("January 1, 2001")
        validate("birthdate")
