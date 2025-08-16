resource "aws_cloudwatch_metric_alarm" "cpu_high" {
  alarm_name = var.alarm_name
  comparison_operator = var.comparison_operator
  evaluation_periods = var.evaluation_periods
  metric_name = "CPUutilization"
  namespace = "AWS/EC2"
  period = var.period
  statistic = var.statistic
  threshold = var.thresold
  alarm_description = var.description
  alarm_actions = var.alarm_actions
  insufficient_data_actions = var.insufficient_data_actions
  dimensions = {
    InstanceId = var.instance_id
  }
}