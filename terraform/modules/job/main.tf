resource "aws_glue_job" "jobname" {
  count                     = length(var.glue_job_script_locations)
  name                      = element(var.glue_job_script_locations, count.index)
  role_arn                  = var.iam_role_arn
  command {
    script_location         = " "
  }
}

