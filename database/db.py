import boto3
 
# Initialize the Glue client
glue_client = boto3.client('glue')
 
response = glue_client.update_database(
 
    Name='ens360-dashboard-db-dev-01',
    DatabaseInput={
        'Name': 'ens360-dashboard-db-dev-01',
        'Description': 'database description updated'
    }
)
