resource "aws_sns_topic" "this" {
  name = var.name
  tags = var.tags
}

resource "aws_sns_topic_subscription" "email" {
  count = var.email==""?0:1
  topic_arn = aws_sns_topic.this.arn
  protocol = "email"
  endpoint = var.email
}