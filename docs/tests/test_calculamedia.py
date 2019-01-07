from ..lms.utils.utils import calculaMedia

def test_calculaMedia():
    assert calculaMedia([8.0]) == 8.0
    assert calculaMedia([10.0,6.0,8.0]) == 8.0
    assert calculaMedia([9.0,6.0,6.0,7.0]) == 7.0
    assert calculaMedia([6.0,6.0,9.0,6.0,6.0,7.0,8.0,8.0]) == 7.0
    assert calculaMedia([10.0,10.0,9.0,9.0,8.0,8.0,7.0,7.0,6.0,6.0]) == 8.0
