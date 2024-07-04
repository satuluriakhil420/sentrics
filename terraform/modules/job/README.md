# AWS Glue Job Terraform Configuration
## Overview
This Terraform configuration creates multiple AWS Glue jobs, each with a specified script location, using a predefined IAM role.

## Requirements
1.Terraform 0.12+
2. AWS account credentials with appropriate permissions
3. Ensure Terraform is installed and AWS credentials are configured properly.
## Usage
## 1.Clone the Repository or Download the Configuration

Clone the repository containing the Terraform configuration:

git clone https://github.com/satuluriakhil420/sentrics.git
cd sentrics/terraform/aws_glue_jobs/
## 2. Initialize Terraform

Initialize Terraform in the directory:
terraform init
## 3. Configure Your Variables

Edit the terraform.tfvars file or create a new .tfvars file to set the required variables:

iam_role_arn = "arn:aws:iam::123456789012:role/your-iam-role"
## 4. Review and Customize main.tf

Edit main.tf to define the AWS Glue job resources based on the glue_job_script_locations variable:

resource "aws_glue_job" "jobname" {
  count     = length(var.glue_job_script_locations)
  name      = element(var.glue_job_script_locations, count.index)
  role_arn  = var.iam_role_arn
  
  command {
    script_location = "s3://your-bucket/path/to/script.py"  # Update with your actual script location
  }
}
Replace "s3://your-bucket/path/to/script.py" with the actual S3 path where your Glue job script resides.

## 5. Apply Terraform Changes

Apply the Terraform configuration to create the AWS Glue jobs:

terraform apply
Confirm by typing yes when prompted.

## 6. Verify in AWS Management Console

Check the AWS Glue console to verify that your Glue jobs were created successfully and configured with the specified script locations.

## 7. Variables
iam_role_arn: The ARN of the IAM role that the Glue jobs will use.

glue_job_script_locations: A list of script locations for the Glue jobs. Each job will be named after the corresponding script location in the list.

Example variables.tf:


variable "iam_role_arn" {
  description = "The ARN of the IAM role"
  type        = string
}

variable "glue_job_script_locations" {
  type    = list(string)
  default = [
    "ens360-dashboard-c1-dev-01",
    "ens360-dashboard-loc-dev-01", 
    "ens360-dashboard-oc-dev-01",
    "ens360-dashboard-pc-dev-01",
    "ens360-dashboard-pg-dev-01",
    "ens360-dashboard-sl-dev-01"
  ]
}
Modify the glue_job_script_locations list in variables.tf to match your specific Glue job script names and update iam_role_arn with your actual IAM role ARN.


