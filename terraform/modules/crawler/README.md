# Terraform AWS Glue Crawler Module

## Overview

This Terraform module automates the setup of AWS Glue resources including databases and crawlers for crawling data stored in Amazon S3 buckets.

## Requirements

- Terraform 0.12+
- AWS account credentials with appropriate permissions

Ensure Terraform is installed and AWS credentials are configured properly.

## Usage

### 1. Clone the repository or download the module

    git clone https://github.com/satuluriakhil420/sentrics.git
    
    cd sentrics/terraform/modules/crawler/
    
### 2. Initialize Terraform

    terraform init
    
### 3. Configure your variables
  Edit the variables.tf file to set your AWS credentials, bucket name, IAM role ARN, and crawler configurations.
  
  Example: variables.tf

    variable "iam_role_arn" {
      description = "The ARN of the IAM role"
      type        = string
    }
    
    variable "bucket_name" {
      description = "The name of the destination S3 bucket"
      type        = string
    }
    
    variable "crawlers" {
      description = "List of crawlers"
      type        = list(object({
        name       = string
        s3_targets = list(string)
        db_name    = string
      }))
      default = [
        {
          name       = "example-crawler"
          s3_targets = ["s3://example-bucket/path/to/data/"]
          db_name    = "example-db"
        }
      ]
    }
### 4. Customize your main.tf
  Edit main.tf to define the resources and configurations for AWS Glue databases and crawlers based on your variables.tf settings.

  Example main.tf:
    
    resource "aws_glue_catalog_database" "example" {
      for_each = toset([for crawler in var.crawlers : crawler.db_name])
      name     = each.value
    }
    
    resource "aws_glue_crawler" "example" {
      for_each      = { for crawler in var.crawlers : crawler.name => crawler }
      database_name = aws_glue_catalog_database.example[each.value.db_name].name
      name          = each.value.name
      role          = var.iam_role_arn
    
      dynamic "s3_target" {
        for_each = each.value.s3_targets
        content {
          path = s3_target.value
        }
      }
    }
### 5. Apply Terraform changes

    terraform apply
    
### 6. Verify in AWS Management Console
Check the AWS Glue console to verify that your databases and crawlers were created successfully.
