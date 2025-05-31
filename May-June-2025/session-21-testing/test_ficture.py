import pytest

# fixture provides reusable test data
# pass it as function argument, which gives a fresh copy each time

@pytest.fixture
def sample_list():
    return [1,2,3]

def test_list_append(sample_list):
    sample_list.append(4)
    assert sample_list == [1,2,3,4]
 
def test_list_remove(sample_list):
    sample_list.remove(1)
    assert sample_list == [2,3]   

    
# let's say you want to run multiple test cases on a
# common data everytime for that you want to use a 
# common data set that we can do with fixture