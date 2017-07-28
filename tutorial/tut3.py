from azure_blob.crypto import CryptoBlob
from azure_blob.blob import AzureBlob

def main():

    azure_blob = AzureBlob("foobar")
    path = "/home/tangingw/azure_blob_storage/test_pdf/"

    """The code below tells the method to upload the pdf file
    from the path /home/tangingw/azure_blob_storage/test_pdf/
    to pdf_upload in foobar container.

    You can any valid Unix regex to upload the files in batch.
    """
    azure_blob.batch_upload(path, "*.pdf", "pdf_upload")


if __name__ == "__main__":
    main()
