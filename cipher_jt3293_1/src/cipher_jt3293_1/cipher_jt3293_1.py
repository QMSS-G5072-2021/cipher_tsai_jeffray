def cipher(text, shift, encrypt=True):
    """
    The Caesar cipher function is an encryption code where it is replaced by a
    letter from the alphabet after a fixed number of positions down the alphabet
    (A then B then C, etc.).

    The parameters are text, shift, and encrypt=True. The text would contain a word or
    phrase that are from the letters of the alphabet, shift would be a number, and
    encrypt=True ensures that this function would shift. If encrypt=False, it will go
    up the alphabet, meaning the opposite direction of encrypt=True. 

    Encrypting:
    cipher('hello', 2, encrypt=True):
    jgnnq

    Decrypting:
    cipher('jgnnq', 2, encrypt=False):
    hello

    """
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    return new_text
