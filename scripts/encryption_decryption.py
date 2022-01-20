from cryptography.fernet import Fernet
import bcrypt
import os

def encrypt_data(data, key):

    f = Fernet(key)
    data = data.encode() # to bytes
    encrypted_data = f.encrypt(data)
    encrypted_enc_data = encrypted_data.decode() # from bytes to string

    return encrypted_enc_data


def decrypt_data(encrypted_data, key):

    f = Fernet(key)
    encrypted_data = encrypted_data.encode()
    data_encoded = f.decrypt(encrypted_data)
    data = data_encoded.decode()

    return data

# encrypt_data("lol",b'JsHt_gpV8itSFQXBmlcnxHZeKTUpK4OKaqS0SRv7zJU=')
# == gAAAAABh6ciGxnz86WgFdKgWsb3EdzVr1abwUn17cXuLC2F-8Yd5T9Qxazlxh5WFItAgsO4_gMQtYSSsPMzbX1leczYiahm4Ow==

# decrypt_data("gAAAAABh6ciGxnz86WgFdKgWsb3EdzVr1abwUn17cXuLC2F-8Yd5T9Qxazlxh5WFItAgsO4_gMQtYSSsPMzbX1leczYiahm4Ow==",b'JsHt_gpV8itSFQXBmlcnxHZeKTUpK4OKaqS0SRv7zJU=')
# == lol
    # f = Fernet(key)
    # f.
    # return

# key = Fernet.generate_key()
# print(key) # = b'JsHt_gpV8itSFQXBmlcnxHZeKTUpK4OKaqS0SRv7zJU='
#
# f = Fernet(key)
#
# textToEncrypt = f.encrypt(b"Hello world !") #b = to bytes
# print(textToEncrypt)
#
# textDecrypted = f.decrypt(textToEncrypt)
# print(textDecrypted.decode())
#
# salt = os.urandom(16)
# print(salt)





# def hash_pass():
#
#     pw = b'69_G0FUCKY0URS3LF_70'
#     salt = bcrypt.gensalt()
#     pw_hashed = bcrypt.hashpw(pw, salt)
#
#     print(salt)
#     print(pw_hashed)
#     print(pw_hashed.decode())
#
# hash_pass()
