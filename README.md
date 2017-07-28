# Azure Blob Storage (HUMAN READABLE) API version 0.0.1

The release of this API does not challenge the status of API [Microsoft] releases, but it improves some aspects of the API so that it is more human readable:
  - Add a layer of encryption to credentials.json using Fernet generated key
  - The Instance loads and decrypts the encryption once it is started.
  - It can do batch uploads with simple regular expression e.g. [Aa-Bb]*.pdf

This API is still in its infant stage. Feel free to contact me at <tangingw.pas@gmail.com> for suggestion. Appreciate constructive feedback.

### Python Dependecies Required:

Before you start using the library, make sure that you have the following python dependecies:
* [Cryptography] - Python Cryptography Package
* [Azure Blob Storage Python SDK] 

### Installation

As I am currently still working on the installation package, you can use as follow:

```sh
$ cd your_project_folder
$ git clone https://github.com/tangingw/azure_storage.git
$ cd 
```

Edit the ```credentials.json``` and enter your credentials from Azure Blob

```sh
{
 "account": <your Azure Blob storage account>
 "primary_key": <primary_key>
 "second_key": <second_key
}
```

Once you have entered the required details to ```credentials.json```, run the following command:
```sh
$ python generate_key.py
Please enter your password:
```
Please enter your password. Once entered the password successfully, it will prompt a message on the screen

```sh
File cred_new.json created!
```

For security purposes, you are encouraged to delete ```credentials.json``` once ```cred_new.json``` is generated. 
### How to use

For users who want to try this eagerly, you can refer to the ```main_azure.py``` in ```example``` folder. But for those who wants to have a step-by-step guidance, you can refer to the tutorial below:

Tutorial 1: Create a Container

In the same folder that you clone this library, you can type tut1.py as your first tutorial python file
```python
from azure_blob.crypto import CryptoBlob
from azure_blob.blob import AzureBlob

def main():
    #Leave it blank if you don't have a name for container
    azure_blob = AzureBlob() 
    azure_blob.create_container("foobar")
    
if __name__ == "__main__":
    main()
```

Tutorial 2: Upload a file to the container

Once you have created a container with the name foorbar succesfully, you can play around with ```tut2.py``` and upload a file to the container.
```python
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
```
Tutorial 3:

Create ```tut3.py``` and upload multiple files to the container
```python
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
```
Tutoral 4: 

Create ```tut4.py``` and List the files stored in the container:

```python
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
    azure_blob.list_blob()


if __name__ == "__main__":
    main()
```

Tutorial 5: Delete A file from the container

Create ```tut5.py``` and Delete a file from the container

```python
from azure_blob.crypto import CryptoBlob
from azure_blob.blob import AzureBlob

def main():

    azure_blob = AzureBlob("foobar")

    """
    You can list the file using a simple method
    """
    blob_name = "foo_bar/xyz.pdf"

    azure_blob.delete(blob_name)


if __name__ == "__main__":
    main()

```

### Development

Want to contribute? Great!

Please contact me at <tangingw.pas@gmail.com> for Pull Request

### Todos

 - Write Test case for this package
 - Work on blob_bytes, blob_stream

License
----

MIT


[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

   [Microsoft]: <https:www.microsoft.com> 
   [Azure Blob Storage Python SDK]: <https://github.com/Azure/azure-storage-python>
   [Cryptography]: <https://cryptography.io/en/latest/>
   
