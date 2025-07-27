terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}
# this is just to use stable terraform version

provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "server1" {
  ami = "ami-08a6efd148b1f7504"
  instance_type = "t2.micro"
  key_name = "server1"
  tags = {
    Name: "SonamVM"
  }
}

# terraform init
# terraform plan
# terraform apply
# terraform destroy