provider "aws" {
  region = "us-east-1"
}

module "s3_backend" {
  source = "./modules/s3-backend"
  prefix = "sonam-basket"
}