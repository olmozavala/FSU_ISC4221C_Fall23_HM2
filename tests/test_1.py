from answers_module import myrec_advanced
import pytest

def test_myrec_advanced():
    assert myrec_advanced(0) == 0
    assert myrec_advanced(1) == 3
    assert myrec_advanced(2) == 5
    assert myrec_advanced(3) == 10
    with pytest.raises(Exception):
        myrec_advanced(-1)