output "instance_public_ip" {
  value = aws_instance.grafana_host.public_ip
}
output "prometheus_url" {
  value = "http://${aws_instance.grafana_host.public_ip}:9090"
}
output "grafana_url" {
  value = "http://${aws_instance.grafana_host.public_ip}:3000"
}