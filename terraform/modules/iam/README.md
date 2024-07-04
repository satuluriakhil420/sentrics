# Terraform AWS IAM Role Module

## Overview

This Terraform module creates an IAM role in AWS with necessary policy attachments for various AWS services.

## Requirements

- Terraform 0.12+
- AWS account credentials with appropriate permissions

Ensure Terraform is installed and AWS credentials are configured properly.

## Usage

### 1. Clone the repository or download the module
    
    git clone https://github.com/satuluriakhil420/sentrics.git
    cd sentrics/terraform/modules/iam_role/
    
### 2. Initialize Terraform

    terraform init

### 3. Configure your variables
  Edit the variables.tf file to customize the IAM role name (rolename) and any other necessary variables.
  
  Example variables.tf:

    
    variable "rolename" {
      description = "Name of the IAM role"
      type        = string
      default     = "sentrics"
    }
    
### 4. Customize your main.tf
  Edit main.tf to define the IAM role resource and attach policies based on your requirements.
  
  Example main.tf:

    
    resource "aws_iam_role" "myrole" {
      name = var.rolename
    
      assume_role_policy = jsonencode({
        "Version": "2012-10-17",
        "Statement": [
          {
            "Action": "sts:AssumeRole",
            "Principal": {
              "Service": "glue.amazonaws.com"
            },
            "Effect": "Allow",
            "Sid": ""
          }
        ]
      })
    }
    
    resource "aws_iam_role_policy_attachment" "s3_policy_attachment" {
      role       = aws_iam_role.myrole.name
      policy_arn = "arn:aws:iam::aws:policy/AmazonS3FullAccess"
    }
    
    resource "aws_iam_role_policy_attachment" "glue_policy_attachment" {
      role       = aws_iam_role.myrole.name
      policy_arn = "arn:aws:iam::aws:policy/service-role/AWSGlueServiceRole"
    }
    
    resource "aws_iam_role_policy_attachment" "gluenotebook_policy_attachment" {
      role       = aws_iam_role.myrole.name
      policy_arn = "arn:aws:iam::aws:policy/service-role/AWSGlueServiceNotebookRole"
    }
    
    resource "aws_iam_role_policy_attachment" "glueconsole_policy_attachment" {
      role       = aws_iam_role.myrole.name
      policy_arn = "arn:aws:iam::aws:policy/AWSGlueConsoleFullAccess"
    }
    
    resource "aws_iam_role_policy_attachment" "service_catalog_policy_attachment" {
      role       = aws_iam_role.myrole.name
      policy_arn = "arn:aws:iam::aws:policy/AWSServiceCatalogAdminFullAccess"
    }
    
    resource "aws_iam_role_policy_attachment" "athena_policy_attachment" {
      role       = aws_iam_role.myrole.name
      policy_arn = "arn:aws:iam::aws:policy/AmazonAthenaFullAccess"
    }
    
    resource "aws_iam_role_policy_attachment" "quicksight_policy_attachment" {
      role       = aws_iam_role.myrole.name
      policy_arn = "arn:aws:iam::aws:policy/service-role/AWSQuicksightAthenaAccess"
    }

### 5. Apply Terraform changes

    terraform apply
    
### 6. Verify in AWS Management Console
 Check the AWS IAM console to verify that your IAM role and policy attachments were created successfully.
