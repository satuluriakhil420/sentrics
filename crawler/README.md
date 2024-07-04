# AWS Glue Crawler Update Script

## Overview

This script updates an AWS Glue crawler configuration using the Boto3 library in Python. It allows you to modify the crawler's settings such as database connection, S3 target, and description.

## Requirements

- Python 3.x
- Boto3 library (`pip install boto3`)

Ensure your AWS credentials are configured properly on your local machine using AWS CLI or environment variables.

## Usage

### 1. Clone the repository or download the script:
   
    git clone https://github.com/satuluriakhil420/sentrics.git

    cd sentrics/crawler

### 2. Install dependencies

    pip install boto3

### 3. Edit the script crawler.py and fill the required variables

### 4. Save your changes and run the script

    python crawler.py

### 5. Check the AWS Glue console or logs to verify that your crawler was updated successfully.

## Customization

Adjust the variables (crawler_name, role, database_name, table_prefix, description, s3_target) according to your AWS Glue crawler configuration needs.

You can extend this script to handle additional targets (e.g., JDBC, MongoDB) or customize error handling and logging as per your requirements.


