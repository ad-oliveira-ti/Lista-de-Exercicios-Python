from e_mail import validar_email

def test_email_valido():
    assert validar_email('antonio@antonio.com.br') is True

def test_email_invalido_arroba():
    assert validar_email('antonio.com') is False

def test_email_invalido_ponto():
    assert validar_email('antonio@antoniocom') is False

