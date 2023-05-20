provider "azurerm" {
  features {}
}

variable "client_id" {
  description = "Service Principal ID"
}
variable "client_secret" {
  description = "Service Principal secret"
}

resource "azurerm_resource_group" "sandbox" {
  name     = "AKSsandbox"
  location = "uksouth"
}

resource "azurerm_kubernetes_cluster" "sandbox" {
  name                = "sandboxcluster"
  location            = azurerm_resource_group.sandbox.location
  resource_group_name = azurerm_resource_group.sandbox.name
  dns_prefix          = "sandboxcluster"

  default_node_pool {
    name                = "default"
    vm_size             = "Standard_B2s"
    os_disk_size_gb     = 30
    node_count          = 1
    enable_auto_scaling = false
  }

  service_principal {
    client_id     = var.client_id
    client_secret = var.client_secret
  }

  tags = {
    environment = "sandbox"
  }
}