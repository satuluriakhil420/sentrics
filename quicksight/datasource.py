import boto3
 

region = 'us-east-1'

client = boto3.client('quicksight',region_name=region)
 
response = client.create_data_source(
    AwsAccountId='533267236958',
    DataSourceId='test123',
    Name='sentrics-data-source-113',
    Type='S3',
    DataSourceParameters={
        'S3Parameters': {
            'ManifestFileLocation': {
                'Bucket': 'aws-glue-assets-533267236958-us-east-1',
                'Key': 'manifest.json'
            },
            'RoleArn': 'arn:aws:iam::533267236958:role/sentrics' 
        }
    },
    Tags=[
        {
            'Key': 'environment',
            'Value': 'dev'
        },
    ]
)
 
print(response)
