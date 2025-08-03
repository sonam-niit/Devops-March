resource "random_id" "suffix" {
  byte_length = 4
}
resource "aws_s3_bucket" "tf_state" {
  bucket = "${var.prefix}-${random_id.suffix.hex}"
  force_destroy = true 
  # to destroy non empty bucket
  tags = {
    Name = "Terraform State Bucket"
  }
}
resource "aws_s3_bucket_versioning" "versioning" {
  bucket = aws_s3_bucket.tf_state.id
  versioning_configuration {
    status = "Enabled"
  }
}