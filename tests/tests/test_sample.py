def test_addition():
    assert 1 + 1 == 2

def test_string():
    assert "selenium".upper() == "SELENIUM"

def test_list():
    items = ["login", "logout", "search"]
    assert len(items) == 3
