from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient
from dotenv import load_dotenv
import os

load_dotenv()
# Replace with your details
search_service= os.getenv('search_service')
index_name = os.getenv('index_name')
api_key = os.getenv("api_key")
# Set up the search client
endpoint = f"https://{search_service}.search.windows.net"
credential = AzureKeyCredential(api_key)
client = SearchClient(endpoint=endpoint, 
                     index_name=index_name,
                     credential=credential)

try:
    # Perform the search and limit to top 1 result
    results = client.search("Binary Search Tree", top=1)  # Fetch only the top result
    
    # Extract and print the top result
    top_result = next(results, None)  # Get the first result or None if no results
    if top_result:
        print(top_result)  # Print the top result
    else:
        print("No results found.")
        
except Exception as e:
    print(f"Error: {str(e)}")