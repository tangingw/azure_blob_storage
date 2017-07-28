import os
import glob
from azure.storage.blob import BlockBlobService
from crypto import CryptoBlob


class AzureBlob(object):
    
    def __init__(self, container_name=None):
     
        self.container_name = container_name
        self.cred_tuple = CryptoBlob.decrypt_credfile()
        self.blob_service = BlockBlobService(
            account_name=self.cred_tuple[0],
            account_key=self.cred_tuple[1]
        )

    def create_container(self, container_name):
          
        self.blob_service.create_container(container_name)

    def upload_blob_path(self, file_name, folder_name=None, **kwargs):
        
        if folder_name is None:
            
            blob_name = file_name.split("/")[-1]
        
        else:
        
            blob_name = folder_name + "/" + file_name.split("/")[-1]
    
        if not self.blob_service.exists(self.container_name, blob_name):
                            
            print "Uploading %s" % file_name

            self.blob_service.create_blob_from_path(
                self.container_name,
                blob_name,
                file_name
            )

            print "File %s uploaded" % file_name
             
        else:
                
            print "File %s exists in container %s" % (file_name, self.container_name)

    def batch_upload(self, path, file_expression, folder_name=None, **kwargs):

        for file in glob.glob(path + file_expression):

            self.upload_blob_path(file, folder_name)

    def list_blob(self):
  
        blobs =[]
        marker = None
 
        while True:
            
       	    batch = self.blob_service.list_blobs(self.container_name, marker=marker)

    	    blobs.extend(batch)

    	    if not batch.next_marker:
    
        	    break

    	    marker = batch.next_marker

        for blob in blobs:

    	    print(blob.name)

    def download_blob_file(self, blob_name, output_filename=None):
        
        if not self.blob_service.exists(self.container_name, blob_name):
            
            print "Blob %s not FOUND!" % blob_name
            exit(2)
        
        print "Downloading %s" % blob_name

        if output_filename == None:
            
            output_filename = blob_name.split("/")[-1]

        self.blob_service.get_blob_to_path(
            self.container_name,
            blob_name,
            output_filename
        )

        print "File %s saved in %s" % (blob_name, output_filename)

    def delete_blob(self, blob_name):

        if not self.blob_service.exists(self.container_name, blob_name):
            
            print "Blob %s not FOUND!" % blob_name
            exit(2)

        confirm_prompt = raw_input("Are you sure you want to delete this (Y/N)?")

        while confirm_prompt != "Y" and confirm_prompt != "N":

            confirm_prompt = raw_input("Please Enter Y or N:")
 
        if confirm_prompt == "Y":

            print "Deleteing %s" % blob_name

            self.blob_service.delete_blob(
                self.container_name,
                blob_name
            )

            print "%s Deleted" % blob_name
        
    def get_blob_metadata(self, blob_name, **kwargs):
        
        return self.blob_service.get_blob_metadata(self.container_name, blob_name)

    def get_blob_properties(self, blob_name, **kwargs):
        
        blob = self.blob_service.get_blob_properties(self.container_name, blob_name)

        return {
            "content_language": blob.properties.content_settings.content_language,
            "content_type": blob.properties.content_settings.content_type,
            "content_encoding": blob.properties.content_settings.content_encoding,
            "content_md5": blob.properties.content_settings.content_md5,
            "content_length": blob.properties.content_length
        }

    def snapshot_blob(self, blob_name, metadata=None):

        blob = self.blob_service.snapshot_blob(
            self.container_name, 
            blob_name, 
            metadata=metadata
        )

        return blob.snapshot #Return snapshot ID
