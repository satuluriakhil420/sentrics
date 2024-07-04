# Quiksite Management Scripts

## Overview

This repository contains management scripts for handling various aspects of a web application (referred to as "quiksite"). Each script focuses on specific functionalities related to accounts, datasets, datasources, and permissions using AWS services like QuickSight and others.

## Scripts

### 1. `account.py`

- **Description:** Manages account subscriptions and configurations for the "quiksite" application using AWS QuickSight.
- **Dependencies:** Requires `boto3` library and AWS credentials configured.

### 2. `dataset.py`
   Description: Creates a dataset in AWS QuickSight for the "quiksite" application.

   Dependencies: Requires boto3 library and AWS credentials configured.

### 3. `datasource.py`
   Description: Registers a datasource in AWS QuickSight for the "quiksite" application.

   Dependencies: Requires boto3 library and AWS credentials configured.

### 4. `permissions.py`
   Description: Registers a user with specific permissions in AWS QuickSight for the "quiksite" application.

   Dependencies: Requires boto3 library and AWS credentials configured.

## Requirements
   Python 3.x
   AWS credentials with permissions for AWS QuickSight operations
# Usage
### 1. Clone the repository:

    git clone https://github.com/satuluriakhil420/sentrics.git

    cd sentrics/quicksight
   
### 2. Install dependencies:

    pip install boto3
   
### 3. Edit each script as needed, replacing placeholders with your actual AWS account details and configurations.


### 4. Run each script individually to perform its respective function within the "quiksite" application.
    python account.py
    
    python dataset.py
    
    python datasource.py
    
    python permission.py
    
## Customization

   Each script can be customized to fit specific requirements of your "quiksite" application.
   
   Modify the scripts to include additional features, integrate with other AWS services, or handle error cases as per your requirements.
