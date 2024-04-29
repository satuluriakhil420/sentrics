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

