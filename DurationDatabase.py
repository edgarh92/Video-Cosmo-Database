import azure.cosmos.cosmos_client as cosmos_client
import azure.cosmos.errors as errors

import os

# Set up the connection to Azure
endpoint = os.environ["COSMOS_ENDPOINT"]
key = os.environ["COSMOS_KEY"]

# Create a database to store the video information
database_name = "my_database"
try:
    database = client.create_database(database_name)
except errors.HTTPFailure as e:
    if e.status_code == 409:
        # Database already exists, so get a reference to it
        database = client.get_database_client(database_name)

# Create a container to store the video information
container_name = "my_container"
try:
    container = database.create_container(
        id=container_name,
        partition_key=PartitionKey(path="/id"),
        offer_throughput=400
    )
except errors.HTTPFailure as e:
    if e.status_code == 409:
        # Container already exists, so get a reference to it
        container = database.get_container_client(container_name)

# Define the video information to be stored in the database
video = {
    "id": "1",
    "name": "My Video",
    "duration": 60,
    "storage_location": "https://mystorageaccount.blob.core.windows.net/videos/myvideo.mp4"
}

# Add the video information to the container
container.upsert_item(video)
