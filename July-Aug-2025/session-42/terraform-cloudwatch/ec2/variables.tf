variable "ami" {type = string}
variable "instance_type" {
    type = string 
    default = "t2.micro"
}
variable "key_name" { type = string}
variable "name" {
  type = string
  default = "tf-ec2"
}
variable "tags" {
  type = map(string)
  default = {}
}
variable "user_data" {
  type = string
  default = <<-EOF
  #!/bin/bash
  yum update -y
  sudo yum install stress -y
  EOF
}
variable "security_group_name" {
  type = string
  default = "tf-ec2-sg"
}
variable "ssh_cidr_blocks" {
  type = list(string)
  default = [ "0.0.0.0/0" ]
}