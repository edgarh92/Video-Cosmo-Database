import azure.cosmos.cosmos_client as cosmos_client
import azure.cosmos.errors as errors
import os

# Set up the connection to Azure
endpoint = os.environ["COSMOS_ENDPOINT"]
key = os.environ["COSMOS_KEY"]

client = cosmos_client.CosmosClient(endpoint, key)

# Get a reference to the database and container
database = client.get_database_client(database_name)
container = database.get_container_client(container_name)

# Define the updated video duration
updated_duration = 90

# Get the current video information from the database
video = container.read_item(video_id, partition_key=PartitionKey(path="/id"))

# Update the video duration
video["duration"] = updated_duration

# Replace the video document in the database with the updated information
container.replace_item(video, video_id, partition_key=PartitionKey(path="/id"))
