# AWS S3 Bucket Terraform Module

This Terraform module creates an AWS S3 bucket with the specified bucket name and access control settings.

## Prerequisites

Before you begin, ensure you have the following:

- AWS credentials configured with sufficient permissions to create S3 buckets.
- Terraform installed on your local machine.

## Usage

### 1. Clone the Repository

Clone this repository to your local machine:

git clone <repository-url>
cd <repository-directory>
### 2. Initialize Terraform
Initialize Terraform in the directory where your .tf files are located:

terraform init
### 3. Modify Variables (Optional)
If you want to use a different bucket name, modify the bucketname variable in variables.tf file.

### 4. Review and Apply Changes
Review the Terraform execution plan to ensure it will create the resources as expected:

terraform plan
If the plan looks good, apply the changes to create the S3 bucket:
terraform apply

### 5. Cleanup (Optional)
If you want to destroy the S3 bucket and remove all associated resources:
terraform destroy

### 6. Outputs
After applying the Terraform configuration, you will get the following output:

bucket_name: The name of the created S3 bucket.
Variables
bucketname: (Default: "dashboard-sl-non-prod-777") Name of the S3 bucket to be created.
