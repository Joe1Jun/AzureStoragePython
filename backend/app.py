# Import necessary libraries
import streamlit as st  # Streamlit is a Python library used to create interactive web apps.
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient  # Azure SDK for interacting with Blob Storage.
from dotenv import load_dotenv  # dotenv is used to load environment variables from a .env file.
import os  # OS module allows interaction with the operating system (fetch environment variables, etc.).

# Load environment variables from a .env file.
# This is a security best practice to avoid hardcoding sensitive information like API keys.
load_dotenv()

# ------------------- Azure Blob Storage Configuration -------------------

# Fetch the storage account URL from environment variables.
# This URL typically follows the format:
# "https://<your_storage_account>.blob.core.windows.net"
account_url = os.getenv("account_url")  

# Fetch the container name from environment variables.
# A container is like a folder in Blob Storage where all the uploaded files will be stored.
container_name = os.getenv('container_name')  

# Fetch the storage account key from environment variables.
# This is used for authentication when accessing Azure Blob Storage.
# ⚠️ Security Note: Instead of using an account key, it is recommended to use Managed Identity.
account_key = os.getenv('account_key')  

# Initialize the BlobServiceClient, which is responsible for interacting with Azure Blob Storage.
# It requires the storage account URL and authentication credentials.
blob_service_client = BlobServiceClient(account_url=account_url, credential=account_key)

# ------------------- Function to Upload Files to Azure Blob Storage -------------------

def upload_file_to_blob(file):
    """
    Uploads a given file to Azure Blob Storage.

    Parameters:
    file (UploadedFile): The file uploaded by the user in Streamlit.

    Returns:
    None (Displays success or error messages in the Streamlit UI).
    """
    try:
        # Create a BlobClient instance, which allows interaction with a specific file (blob) in the container.
        # The 'blob' parameter specifies the filename (same as the uploaded file).
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=file.name)

        # Upload the file to Azure Blob Storage.
        # The "overwrite=True" parameter ensures that if a file with the same name exists, it will be replaced.
        blob_client.upload_blob(file, overwrite=True)

        # Display a success message in Streamlit once the upload is complete.
        st.success(f"File '{file.name}' uploaded successfully!")

    except Exception as e:
        # If an error occurs during the upload process, display an error message in Streamlit.
        st.error(f"Error: {str(e)}")

# ------------------- Streamlit UI (User Interface) -------------------

# Set the title of the Streamlit app.
# This will be displayed as a heading on the web page.
st.title("Upload File to Azure Blob Storage")

# Create a file uploader widget in Streamlit.
# Users can select a file from their device and upload it.
# The 'type' parameter restricts the file formats to text, PDFs, and image files.
uploaded_file = st.file_uploader("Choose a file to upload", type=["txt", "pdf", "jpg", "png", "jpeg"])

# Check if a file has been uploaded by the user.
if uploaded_file is not None:
    # Display the file name as feedback to the user.
    st.write(f"Uploaded file: {uploaded_file.name}")

    # Call the function to upload the file to Azure Blob Storage.
    upload_file_to_blob(uploaded_file)
