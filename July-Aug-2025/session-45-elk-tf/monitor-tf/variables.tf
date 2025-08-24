locals {
  region="us-east-1"
  instance_type="t2.micro"
  key_name="linuxkey"
}

variable "allowed_cidrs" {
  description = "List of CIDR blocks allowed to access"
  type = list(string)
  default = [ "0.0.0.0/0" ]
}