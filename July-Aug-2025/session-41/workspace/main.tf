provider "aws" {
  region = var.region
}
resource "aws_s3_bucket" "demo" {
  bucket = "${var.bucket_name}-${terraform.workspace}"
}