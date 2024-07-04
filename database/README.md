# AWS Glue Database Update Script

## Overview

This script updates an AWS Glue database configuration using the Boto3 library in Python. It allows you to modify the database's name and description.

## Requirements

- Python 3.x
- Boto3 library (`pip install boto3`)

Ensure your AWS credentials are configured properly on your local machine using AWS CLI or environment variables.

## Usage

### 1. Clone the repository or download the script:
   
    git clone https://github.com/your-username/aws-glue-database-update.git
    cd aws-glue-database-update
 
### 2. Install Dependencies:

    pip install boto3

### 3. Edit the script db.py and fill in the required variables:

### 4. Save your changes and run the script:

    python db.py

### 5. Check the AWS Glue console or logs to verify that your database was updated successfully.

## Customization

   Adjust the variables (database_name, new_name, new_description) according to your AWS Glue database configuration needs.

   You can extend this script to handle additional database operations or customize error handling and logging as per your requirements.

