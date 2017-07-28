from azure_blob.crypto import CryptoBlob
from azure_blob.blob import AzureBlob


def main():
    
    azure_blob = AzureBlob("test-pdf")
    path = "/home/tangingw/azure_storage_github/test_pdf/"

    #azure_blob.batch_upload(path, "*.pdf", "pdf_upload")
    #azure_blob.download_blob_file("pdf_upload/Chef.pdf", "Chef.pdf")
    #azure_blob.list_blob()

    azure_blob.upload_blob_path("Chef.pdf", "pdf_upload")
    
    #print azure_blob.get_blob_properties("pdf_upload/Hadoop_in_the_Enterprise_Architecture.pdf")


if __name__== "__main__":
    main()
