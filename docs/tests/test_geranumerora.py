from ..lms.utils.utils import geraNumeroRA

def test_geraNumeroRa():
    assert geraNumeroRA(1800020) == 1800021
    assert geraNumeroRA(1701234) == 1800001
    assert geraNumeroRA("") == 1800001
    assert geraNumeroRA(1800999) == 1801000
    assert geraNumeroRA(1801234) == 1801235