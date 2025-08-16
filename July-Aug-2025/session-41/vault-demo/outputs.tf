output "database_password" {
  value = data.vault_kv_secret.db.data
  sensitive = true
}