variable "region" {
  type = string
  default = "us-east-1"
}
variable "ami" {
  type = string
}
variable "instance_type" {
  type = string
  default = "t2.micro"
}
variable "key_name" {
  type = string
}
variable "email" {
  type = string
}