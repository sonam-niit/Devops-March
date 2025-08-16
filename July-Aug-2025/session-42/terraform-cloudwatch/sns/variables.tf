variable "name" {
  type = string
  default = "ec2-cpu-alerts"
}
variable "email" {
  type = string
  default = ""
}
variable "tags" {
  type = map(string)
  default = {}
}