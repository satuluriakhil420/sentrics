module "iam" {
  source = "./iam"
}

module "gluejob" {
  source = "./job"
  iam_role_arn = module.iam.myrole_arn
}

module "gluecrawler" {
  source = "./crawler"
  iam_role_arn = module.iam.myrole_arn
  bucket_name  = module.s3.bucket_name
}

module "s3" {
  source = "./s3"
}

