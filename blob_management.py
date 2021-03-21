import os
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__
from azure.core import exceptions


class SasToBlob:

    def __init__(self):
        # Retrieve the connection string for use with the application. The storage
        # connection string is stored in an environment variable on the machine
        # running the application called AZURE_STORAGE_CONNECTION_STRING. If the environment variable is
        # created after the application is launched in a console or with Visual Studio,
        # the shell or application needs to be closed and reloaded to take the
        # environment variable into account.
        try:
            print("Azure Blob Storage v" + __version__)
        except Exception as ex:
            print('Exception:')
            print(ex)

        # Connecting to azure storage account with connecting string
        self.connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
        print(self.connect_str)

        # Create the BlobServiceClient object which will be used to create a container client
        self.blob_service_client = BlobServiceClient.from_connection_string(self.connect_str)

    def create_container(self, container_name):

        try:
            # Create the container
            self.blob_service_client.create_container(container_name)
        except exceptions.ResourceExistsError:
            print('The specified container already exists.')

    def upload_files(self, local_path, local_file_name, container_name, overwrite):

        print("Trying to Upload file(s) to Azure Storage container " + container_name + ":")
        print('\tfiles:')
        for file in local_file_name:
            try:
                upload_file_path = os.path.join(local_path, file)
                # Create a blob client using the local file name as the name for the blob
                blob_client = self.blob_service_client.get_blob_client(container=container_name, blob=file)
                # Upload the created file
                with open(upload_file_path, "rb") as data:
                    blob_client.upload_blob(data, overwrite=overwrite)
                    print("\t\t- " + file + ' is uploaded.')
            except exceptions.ResourceExistsError:
                print('The specified blob "' + local_file_name + '" already exists.')
        print('\n')

    def upload_folders(self, local_path, container_name, overwrite):

        print("Trying to Upload folder(s) to Azure Storage container " + container_name + ":")
        for path, d, files in os.walk(local_path):
            if files:
                folder = os.path.basename(os.path.normpath(local_path))
                print('\tfolder: '+local_path)
                print('\tfiles:')
                for file in files:
                    try:
                        upload_file_path = os.path.join(local_path, file)
                        file_path = os.path.join(folder, file)
                        blob_client = self.blob_service_client.get_blob_client(container=container_name, blob=file_path)
                        with open(upload_file_path, "rb") as data:
                            blob_client.upload_blob(data, overwrite=overwrite)
                            print("\t\t- " + file + ' is uploaded.')
                    except exceptions.ResourceExistsError:
                        print('The specified blob "' + file + '" already exists.')
            else:
                print('The folder is empty, cannot be uploaded.')
        print('\n')
