# app.py
# This is a test commit
def add(a, b, c):
    d=1
    return a + b + c

def test_add():
    assert add(1, 2, 3) == 6
    assert add(1, -1, 0) == 0
