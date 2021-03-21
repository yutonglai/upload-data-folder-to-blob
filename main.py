from blob_management import SasToBlob
import yaml


# Load parameters
param = yaml.load(open('param.yml'), Loader=yaml.FullLoader)
container_name = param['container_name']
local_path = param['source_path']
dataset = param['dataset']

# Initialization object SasToBlob
dt = SasToBlob()

# Create a unique name for the container
dt.create_container(container_name)

# Upload specified files to blob
dt.upload_files(local_path, dataset, container_name, overwrite=True)

# Upload entire folder
dt.upload_folders(local_path, container_name, overwrite=True)

