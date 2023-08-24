variable "s1" {
  type = set(string)
  default = ["hoe", "fue", 1]
}

locals {
  m1 = {
    "k1" = {},
    "k2" = {
      p1 = 1
    },
  }
  m1_keys = toset(keys(local.m1))
}

output "s1" {
  value = var.s1
}

output "m1" {
  value = local.m1_keys
}
