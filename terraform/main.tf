variable "s1" {
  type = set(string)
  default = ["hoe", "fue", 1]
}

output "s1" {
  value = var.s1
}
