provider "aws" {
  region = local.region
}
resource "aws_security_group" "elk_sg" {
  name = "elk-sg"
  dynamic "ingress" {
    for_each = var.allowed_cidrs
    content {
        description = "SSH"
        from_port = 22
        to_port = 22
        protocol = "tcp"
        cidr_blocks = [ingress.value]
    }
  }
  dynamic "ingress" {
    for_each = var.allowed_cidrs
    content {
        description = "Grafana"
        from_port = 3000
        to_port = 3000
        protocol = "tcp"
        cidr_blocks = [ingress.value]
    }
  }
  dynamic "ingress" {
    for_each = var.allowed_cidrs
    content {
        description = "Prometheus"
        from_port = 9090
        to_port = 9090
        protocol = "tcp"
        cidr_blocks = [ingress.value]
    }
  }
  egress {
    from_port = 0
    to_port = 0
    protocol = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

data "aws_ami" "ubuntu" {
  most_recent = true
  owners      = ["099720109477"]
  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd/ubuntu-jammy-22.04-amd64-server-*"] 
  }
  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }
}
resource "aws_instance" "grafana_host" {
  ami = data.aws_ami.ubuntu.id
  instance_type = local.instance_type
  key_name = local.key_name
  vpc_security_group_ids = [ aws_security_group.elk_sg.id ]
  user_data = file("${path.module}/user_data.sh")
}