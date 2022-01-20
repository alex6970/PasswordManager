from cryptography.fernet import Fernet
import bcrypt
import os

def encrypt_data():
    return

# key = Fernet.generate_key()
# print(key)
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
