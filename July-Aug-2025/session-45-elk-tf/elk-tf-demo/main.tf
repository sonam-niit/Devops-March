provider "aws" {
  region = var.region
}
resource "aws_security_group" "elk_sg" {
  name = "elk-sg"
  ingress {
    from_port = 22
    to_port = 22
    protocol = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  ingress {
    from_port = 9200
    to_port = 9200
    protocol = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  ingress {
    from_port = 5601
    to_port = 5601
    protocol = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  egress {
    from_port = 0
    to_port = 0
    protocol = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}
resource "aws_instance" "elk" {
  ami = "ami-020cba7c55df1f615"
  instance_type = "t3.medium"
  key_name = "linuxkey"
  vpc_security_group_ids = [aws_security_group.elk_sg.id]
  user_data = file("${path.module}/user_data.sh")
  root_block_device {
    volume_size = 40
    volume_type = "gp3"
  }

  tags = {
    Name="ELK-Instance"
  }
}