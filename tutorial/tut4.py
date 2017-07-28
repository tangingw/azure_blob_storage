from azure_blob.crypto import CryptoBlob
from azure_blob.blob import AzureBlob

def main():

    azure_blob = AzureBlob("foobar")

    """
    You can list the file using a simple method.
    """
    azure_blob.list_blob()


if __name__ == "__main__":
    main()
