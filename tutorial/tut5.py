from azure_blob.crypto import CryptoBlob
from azure_blob.blob import AzureBlob

def main():
 
    azure_blob = AzureBlob("foobar")

    """
    You can delete the file using a simple method
    """
    blob_name = "foo_bar/xyz.pdf"

    azure_blob.delete_blob(blob_name)


if __name__ == "__main__":
    main()
