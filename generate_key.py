import getpass
from azure_blob.crypto import CryptoBlob


def main():

    password = getpass.getpass("Please enter your password:")
    CryptoBlob.encrpyt_credfile(password)


if __name__ == '__main__':

    main()