locals {
  instance_type="t3.medium"
  region="us-east-1"

#   env="dev"
#   extra examples of locals
#   bucket_name="${local.env}-${local.region}-bucket"
#   instance_count=length(var.subnets)*2
}

# variable "subnets" {
#   default = []
# }

variable "allowed_cidrs" {
  description = "List of CIDR blocks allowed to access"
  type = list(string)
  default = [ "0.0.0.0/0" ]
}