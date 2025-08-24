output "ec2_public_ip" {
  value = aws_instance.elk.public_ip
}
output "kibana_url" {
  value = "http://${aws_instance.elk.public_ip}:5601"
}
output "elasticsearch_url" {
  value = "http://${aws_instance.elk.public_ip}:9200"
}