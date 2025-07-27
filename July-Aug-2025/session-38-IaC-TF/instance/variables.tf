variable "aws_region" {
  description = "AWS Region"
  default = "us-east-1"
}

variable "ami_id" {
  description = "AMI ID for Ubuntu"
  type = string
}

variable "instance_type" {
  description = "EC2 Instance Type"
  default = "t2.micro"
}

variable "key_name" {
  description = "EC2 Key pair name"
  type = string
}

variable "name_instance" {
  description = "name of the instance"
  default = "WebServer"
}