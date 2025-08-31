provider "aws" {
  region = "us-east-1"
}

module "ec2_instances" {
  source = "./ec2"
  instance_count = 2
}
module "alb" {
  source = "./elb"
  subnet_ids = module.ec2_instances.subnet_ids
  vpc_id = module.ec2_instances.vpc_id
  instance_ids = module.ec2_instances.instance_ids
  target_group_ports = [80]
}