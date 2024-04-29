import boto3
 
glue_client = boto3.client('glue')
 
crawler_name = 'ens360-dashboard-crawler-dev-01'
role = 'arn:aws:iam::533267236958:role/sentrics'  
database_name = 'ens360-dashboard-db-dev-01'
table_prefix = 'crawler_output'
 

description = "description for ens360-dashboard-crawler"

s3_target = {
    'Path': 's3://dashboard-sl-non-prod-777/',
    'Exclusions': []
}
 
response = glue_client.update_crawler(
    Name=crawler_name,
    Role=role,
    DatabaseName=database_name,
    Description=description,
    Targets={
        'S3Targets': [s3_target],
        'JdbcTargets': [],
        'MongoDBTargets': [],
        'DynamoDBTargets': [],
        'CatalogTargets': []
    },
    TablePrefix=table_prefix
)
 
print("Crawler created successfully.")
