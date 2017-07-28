from azure_blob.crypto import CryptoBlob
from azure_blob.blob import AzureBlob

def main():
    #Leave it blank if you don't have a name for container
    azure_blob = AzureBlob()
    azure_blob.create_container("foobar")

if __name__ == "__main__":
    main()
