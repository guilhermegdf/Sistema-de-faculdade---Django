from ..lms.utils.utils import desconta

def test_desconta():
    assert desconta(8,30) == 5.6
    assert desconta(10,20) == 8.0
    assert desconta(7,25) == 5.25
    assert desconta(8.5,30) == 5.95
    assert desconta(6,20) == 4.8