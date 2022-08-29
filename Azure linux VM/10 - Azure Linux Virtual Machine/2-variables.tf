
variable "business_division" {
    type = string
    description = "Business_Division for which this Infrastructure belongs to"
    default = "cloud"
}

variable "environment" {
    type = string
    description = "Environment variable used as a prefix"
    default = "dev"
}

variable "resource_group_name" {
    type = string
    description = "resource group name"
    default = "rg-default"
}

variable "resource_group_location" {
    type = string
    description = "resource group location"
    default = "eastus2"
}