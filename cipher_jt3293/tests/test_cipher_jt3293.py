from cipher_jt3293 import cipher_jt3293

def test_singleword_cipher():
    example = 'hello'
    number = 2
    expected = 'jgnnq'
    actual = cipher(example, number, encrypt=True)
    assert actual == expected 
