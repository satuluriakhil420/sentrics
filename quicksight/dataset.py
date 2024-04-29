import boto3
from datetime import datetime

region = 'us-east-1'
 
client = boto3.client('quicksight',region_name=region)
 
dataset_params = {
    'AwsAccountId': '533267236958',
    'DataSetId': 'sentrics-1185-data-set',
    'Name': 'sentrics-dataset-1185-name',
    'PhysicalTableMap': {
        'string': {
            'S3Source': {
                'DataSourceArn': 'arn:aws:quicksight:us-east-1:533267236958:datasource/test123',  
                'UploadSettings': {
                    'Format': 'CSV',  
                    'StartFromRow': 1,  
                    'ContainsHeader': True,
                    'TextQualifier': 'DOUBLE_QUOTE',  
                    'Delimiter': ','  
                },
                'InputColumns': [
                    {
                        'Name': 'column_name',
                        'Type': 'STRING',  
                    },
                ]
            }
        }
    },
    'ImportMode': 'SPICE',  
}
 
response = client.create_data_set(**dataset_params)
 
print(response)
