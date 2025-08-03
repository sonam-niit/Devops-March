output "bucket_name" {
  description = "The Name of the bucket"
  value = aws_s3_bucket.website_bucket.bucket
}
output "bucket_arn" {
  description = "ARN of S3 Bucket"
  value = aws_s3_bucket.website_bucket.arn
}
# This one is deprecated
output "endpoint"{
  value = aws_s3_bucket.website_bucket.website_endpoint
}
# you can use below with website configuration
output "website_url" {
  description = "Static Website Endpoint"
  value = aws_s3_bucket_website_configuration.website_config.website_endpoint
}