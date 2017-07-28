import os.path
import base64
import json
import yaml
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend


class Crypto(object):

    @staticmethod
    def generate_key(password):

        if len(password) < 8:

            return "Password Length is less than 8"

        digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
        digest.update(password)

        return base64.urlsafe_b64encode(digest.finalize())

    @staticmethod
    def encrypt(message, key):

        key_token = Fernet(key)
        cipher_text = key_token.encrypt(message)

        return cipher_text

    @staticmethod
    def decrypt(cipher_text, key):

        key_token = Fernet(key)

        return key_token.decrypt(bytes(cipher_text))


class CryptoBlob(Crypto):

    @staticmethod
    def encrpyt_credfile(password):
    
        if not os.path.exists("credentials/credentials.json"):

            print "credentials.json not found!"
            exit(2)

        file = open("credentials/credentials.json", "r")

        plain_cred = json.loads(file.read()) 
        key = Crypto.generate_key(password)

        credential = dict(
            account=plain_cred["account"],
            key=key,
            primary_key=Crypto.encrypt(bytes(plain_cred["primary_key"]), key)
        )

        file.close()

        with open("credentials/cred_new.json", "w") as crypto_file:

            crypto_file.write(
                json.dumps(
                    credential,
                    sort_keys=True,
                    indent=4,
                    separators=(',' , ': ')
                )
            )

        print "File cred_new.json created!"

    @staticmethod
    def decrypt_credfile():

        if not os.path.exists("credentials/cred_new.json"):

            return "cred_new.json not found! Please generate new cred_new.json with generate_credfile"

        with open("credentials/cred_new.json", "r") as crypto_file:

            yaml_dict = yaml.safe_load(crypto_file.read())

        return (
            yaml_dict["account"],
            Crypto.decrypt(yaml_dict["primary_key"], yaml_dict["key"])
        )
