from cipher_jt3293_1 import cipher_jt3293_1

def test_singleword_cipher():
    example = 'hello'
    number = 2
    expected = 'jgnnq'
    actual = cipher_jt3293_1.cipher(example, number, encrypt=True)
    assert actual == expected 

