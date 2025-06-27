from email_utils import is_valid_email

def test_valid_email():
    assert is_valid_email("test@example.com") is True

def test_invalid_email():
    assert is_valid_email("invalid-email") is False
