from azure_blob.crypto import CryptoBlob
from azure_blob.blob import AzureBlob

def main():
 
    azure_blob = AzureBlob("foobar")

    """
    You can download the file using a simple method
    """
    blob_name = "foo_bar/xyz.pdf"

    azure_blob.download_blob_file(blob_name)

    """
    If you want to save the blob_name to other
    output name, you can add as following:
    """
    
    azure_blob.download_blob_file(blob_name, output_filename="abc.pdf")

if __name__ == "__main__":
    main()
