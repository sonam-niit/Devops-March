variable "bucket_name" {
  type = string
  description = "The name of the S3 Bucket"
}
variable "aws_region" {
  type = string
  default = "us-east-1"
}
variable "environment" {
  type = string
  default = "dev"
}