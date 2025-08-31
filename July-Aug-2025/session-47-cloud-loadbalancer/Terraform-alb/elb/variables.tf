variable "subnet_ids" {
  type = list(string)
}
variable "vpc_id" {
  type = string
}
variable "instance_ids" {
  type = list(string)
}
variable "target_group_ports" {
  type = list(number)
}