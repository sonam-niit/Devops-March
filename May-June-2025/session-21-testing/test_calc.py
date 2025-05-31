import pytest
from calculator import add, sub, mul, div

def test_add():
    assert add(2,3) == 5
    assert add(-1,1) == 0
    assert add(0,0) == 0
    
def test_sub():
    assert sub(5,3) == 2
    assert sub(0,4) == -4
    assert sub(-1,1) == -2
    
# write test case for multiplication by your own
def test_div():
    assert div(6,3) == 2
    assert div(10,2) == 5

def test_div_zero():
    with pytest.raises(ValueError):
        div(10,0)
        
## using pytest.raises to check exception
## verify functions fails with invalid inputs