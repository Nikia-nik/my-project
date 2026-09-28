from example import fard_zoj, add
import pytest
@pytest.mark.slow
def test_fard_zoj()-> None:
    assert fard_zoj(4) is True

@pytest.mark.slow
def test_fard()-> None:
    assert fard_zoj(5) is False
#اسم تست ها باید فرق کنه 
#pytest *file name* 
#مثال:
#pytest text_example.py
#-x
#-v

#from example import add
#def test_add()->None:
    #assert add(2,5) == 7
#parametrize


#@pytest.mark.slow
#it doesnt need to be slow , it can be any word
#it's like you are marking them
#pytest -m slow
#so you only test those who are marked by the name you chose
@pytest.mark.parametrize(
    "a,b,result",
    [
        (1,200,201),
        (101,203,304),
        (2,7,9)
    ]
)

def test_add(a,b,result):
    assert add(a,b) == result
