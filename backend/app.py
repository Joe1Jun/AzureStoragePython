import streamlit as st
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
from dotenv import load_dotenv
import os


load_dotenv()

# Set up your Azure Blob Storage details
account_url = os.getenv("account_url") #  Replace with your actual account URL
container_name = os.getenv('container_name')  # Replace with your actual container name
account_key = os.getenv('account_name')  # Replace with your actual account key (either Key1 or Key2)

# Initialize the BlobServiceClient
blob_service_client = BlobServiceClient(account_url=account_url, credential=account_key)

# Function to upload file to Azure Blob Storage
def upload_file_to_blob(file):
    try:
        # Create a BlobClient using the container name and file name
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=file.name)

        # Upload the file to Blob Storage
        blob_client.upload_blob(file, overwrite=True)

        st.success(f"File {file.name} uploaded successfully!")
    except Exception as e:
        st.error(f"Error: {str(e)}")

# Streamlit UI
st.title("Upload File to Azure Blob Storage")

# File uploader widget in Streamlit
uploaded_file = st.file_uploader("Choose a file to upload", type=["txt", "pdf", "jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Display the file name and upload it
    st.write(f"Uploaded file: {uploaded_file.name}")
    upload_file_to_blob(uploaded_file)
