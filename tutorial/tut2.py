from azure_blob.crypto import CryptoBlob
from azure_blob.blob import AzureBlob

def main():

    """ You can put your container name once you
    have the container name 'foobar'
    """

    azure_blob = AzureBlob("foobar")

    """The code below means create a folder called pdf_upload on
    container 'foobar'and upload xyz.pdf to pdf_upload.
    Alternatively if you can put the file to the blob without the folder
    """
    azure_blob.upload_blob_path("xyz.pdf", "pdf_upload")
    azure_blob.upload_blob_path("xyz.pdf")

if __name__ == "__main__":
    main()

