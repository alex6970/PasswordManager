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

def check_key(key):
    ''' Ensure that the login private key is the right one (not mandatory, just to tell user if it's the rigght key)'''
    try:
        f = Fernet(key)
        decrypted = f.decrypt(b"gAAAAABh8H_hQAXA7goWF2zaMqSIrDRYZxUpIRo0_4nkMpLIxPHULc6Vmsaxi_hGF3wTN6SQ2TiA_d2oQF4YGVPzQKt8lvGNkg==")
        return True
    except:
        return False
