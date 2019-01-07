from ..lms.utils.utils import calculaMediaFinal

def test_calculaMediaFinal():
    assert calculaMediFinal(10, 10) == 10
    assert calculaMediFinal(3, 7) == 4.6
    assert calculaMediFinal(-10, 0) == None
    assert calculaMediFinal(12, 7) == None
    assert calculaMediFinal(0, 0) == 0
    assert calculaMediFinal(6, 4) == 5.2
    assert calculaMediFinal(5, 5) == 5

