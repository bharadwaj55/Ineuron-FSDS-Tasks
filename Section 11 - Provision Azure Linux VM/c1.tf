terraform {
  required_providers {
    azurerm = {
      source = "hashicorp/azurerm"
      version = "3.18.0"
    }
    random = {
        source = "hashicorp/random"
        version = ">= 3.0"
    }
  }
}

provider "azurerm" {
  # Configuration options
  features {
  }
}

resource "random_string" "myrandom" {
  length           = 16
  lower = true
  special          = false
  upper = false
  numeric = true

}

