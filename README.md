## upload-data-folder-to-blob
This project creates connectors to upload data or folders from local to Azure Storage. 


### Authorize request from application to Azure storage account
It's necessary to set up connection between local machine and the Azure storage account before hand.
#### Step 1
* Sign in Azure potal -> Storage Account -> Settings -> Access keys -> Connection string
* Copy the connection string.
#### Step 2
* Write it into a new environment variable on local machine. In Windows, open cmd, run:
```
  setx AZURE_STORAGE_CONNECTION_STRING "<yourconnectionstring>"
```
#### Step 3
* Restart any application that will use this env vriable, eg. IDE etc.


### SasToBlob Class
The class provide methods for creating container, uploading files or folders from local machine to Azure Storage.
#### Methods
* create_container
* upload_files
  * Files can be replaced by setting overwrite=True
* upload_folders
  * Files inside folders can be replaced by setting overwrite=True
#### Parameters
```
container_name
local_path 
dataset 
overwrite
```
