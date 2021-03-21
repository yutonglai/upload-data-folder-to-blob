## upload-data-folder-to-blob
This project creates connectors to upload data or folders from local to Azure Storage. 
### Authorize request from application to Azure storage account
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
