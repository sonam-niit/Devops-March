provider "local" {}

resource "local_file" "sample" {
  filename = "hello.txt"
  content = "Hello From terraform!"
}

# open this folder in wsl
# run below commands: terraform init
# teraform plan
# terraform apply (say yes)
# see the hello.txt file created
# terraform destroy (hello.txt must be destroyed)