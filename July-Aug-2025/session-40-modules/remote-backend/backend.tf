terraform {
  backend "s3" {
    bucket = "sonam-basket-d8c0c54a"
    key = "terraform.tfstate"
    region = "us-east-1"
  }
}