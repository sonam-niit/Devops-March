provider "vault" {
  address = "http://127.0.0.1:8200"
  token = var.VAULT_TOKEN #should take value for environment variables
}
data "vault_kv_secret" "db" {
  path = "enter your secret URL here"
}