## Init and Apply
terraform init
terraform apply --auto-approve

# Save output
BUCKET_NAME=$(terraform output -raw bucket_name)

# Create File Dynamically
cat > backend.tf <<EOF
terraform{
    backend "s3" {
        bucket = "$BUCKET_NAME"
        key = "terraform.tfstate"
        region =  "us-east-1"
    }
}
EOF

# Init Again
terraform init

# you need to say yes manually here