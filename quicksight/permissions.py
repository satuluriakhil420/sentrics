import boto3
 
client = boto3.client('quicksight', region_name='us-east-1')
 
response = client.register_user(
    IdentityType='QUICKSIGHT',
    Email='test@gmail.com',
    UserRole='READER',
    AwsAccountId='533267236958',
    Namespace='default',
    UserName='akhil',
    Tags=[
        {
            'Key': 'Environment',
            'Value': 'Dev'
        }
    ]
)
 
print("User registered:", response)
