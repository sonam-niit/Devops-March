output "instance_public_ip" {
  description = "The Public IP of my Webserver"
  value = aws_instance.server1.public_ip
}
output "instance_dns" {
  description = "Instance Domain Name"
  value = aws_instance.server1.public_dns
}