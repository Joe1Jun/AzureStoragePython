from azure.storage.blob import BlobServiceClient
import os
from dotenv import load_dotenv

load_dotenv()

# Load environment variables (account_url and container_name) from .env
account_url = os.getenv("account_url")
container_name = os.getenv("container_name")
account_key = os.getenv("account_key")

# Initialize the BlobServiceClient
blob_service_client = BlobServiceClient(account_url=account_url, credential=account_key)

# Fetch text from a specific blob (file)
def get_blob_text(blob_name):
    try:
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)
        blob_data = blob_client.download_blob()
        content = blob_data.readall().decode('utf-8')  # Assuming text is stored as UTF-8
        return content
    except Exception as e:
        print(f"Error reading blob: {str(e)}")
        return None

# Example: Fetch text from a file
blob_name = "Algorithmics_ The Spirit of Computing (3rd ed.) [Harel & Feldman 2004-06-11].pdf"  # Replace with the actual blob name
text = get_blob_text(blob_name)
print(text)
