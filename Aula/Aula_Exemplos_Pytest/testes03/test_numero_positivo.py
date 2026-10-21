from numero_positivo import positivo

def test_verdadeiro_positivo():
    assert positivo(5) is True

def test_falso_positivo():
    assert positivo(-5) is False

def test_zero_positivo():
    assert positivo(0) is False

def test_verdadeiro_positivo_erro():
    assert positivo(-5) is True

def test_falso_positivo_erro():
    assert positivo(5) is False

def test_zero_positivo_erro():
    assert positivo(99) is False