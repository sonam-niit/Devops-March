resource "aws_instance" "this" {
  ami=var.ami
  instance_type = var.instance_type
  key_name = var.key_name
  tags = merge({Name=var.name},var.tags)
  user_data = var.user_data
  vpc_security_group_ids = [aws_security_group.this.id]
}
resource "aws_security_group" "this" {
  name = var.security_group_name
  description = "Allow SSH for EC2"
  ingress {
    from_port = 22
    to_port = 22
    protocol = "tcp"
    cidr_blocks = var.ssh_cidr_blocks
  }
  egress {
    from_port = 0
    to_port = 0
    protocol = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
  tags = var.tags
}