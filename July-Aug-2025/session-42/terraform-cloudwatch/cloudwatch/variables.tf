variable "instance_id" {
  type = string
}
variable "alarm_name" {
  type = string
  default = "ec2-high-cpu"
}
variable "comparison_operator" {
  type = string
  default = "GreaterThanOrEqualToThresold"
}
variable "evaluation_periods" {
  type = number
  default = 2
}
variable "period" {
  type = number
  default = 300
}
variable "thresold" {
  type = number
  default = 80
}
variable "description" {
  type = string
  default = "Trigger When EC2 CPU exceeds 80%"
}
variable "statistic" {
  type = string
  default = "Average"
}
variable "alarm_actions" {
  type = list(string)
  default = []
}
variable "insufficient_data_actions" {
  type = list(string)
  default = []
}