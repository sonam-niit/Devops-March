provider "aws" {
  region = var.region
}
module "ec2" {
  source = "./ec2"
  ami = var.ami
  instance_type = var.instance_type
  key_name =  var.key_name
  name = "cpu-test-ec2"
  tags = {Environment = "dev"}
}
module "sns" {
  source = "./sns"
  name = "ec2-cpu-alerts"
  email = var.email
  tags = {Environment="dev"}
}
module "cloudwatch" {
  source = "./cloudwatch"
  instance_id = module.ec2.instance_id
  alarm_actions = [module.sns.topic_arn]
  alarm_name = "ec2-high-cpu-${module.ec2.instance_id}"
  comparison_operator = "GreaterThanOrEqualToThreshold"
  evaluation_periods=1
  period = 60
  statistic = "Average"
  thresold = 80
  description = "EC2 CPU>=80% for 5 Min"
}