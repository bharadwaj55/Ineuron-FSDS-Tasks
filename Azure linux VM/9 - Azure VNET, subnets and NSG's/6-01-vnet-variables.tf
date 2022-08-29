# Virtual network name
variable "vnet_name" {
    type = string
    description = "Virtual network name"
    default = "vnet-default"  
}
# Virtual network address space
variable "vnet_address_space" {
    type = list(string)
    description = "Virtual network address space"
    default = ["10.0.0.0/16"]
}

# Web subnet name
variable "web_subnet_name" {
    type = string
    description = "Web subnet name"
    default = "websubnet"  
}
# Web subnet address space
variable "web_subnet_address" {
    type = list(string)
    description = "Web subnet address space"
    default = ["10.0.1.0/24"]
}


# App subnet name
variable "app_subnet_name" {
    type = string
    description = "App subnet name"
    default = "appsubnet"  
}
# App subnet address space
variable "app_subnet_address" {
    type = list(string)
    description = "App subnet address space"
    default = ["10.0.11.0/24"]
}


# Database subnet name
variable "db_subnet_name" {
    type = string
    description = "db subnet name"
    default = "dbsubnet"  
}
# Database subnet address space
variable "db_subnet_address" {
    type = list(string)
    description = "db subnet address space"
    default = ["10.0.21.0/24"]
}


# Bastion subnet name
variable "bastion_subnet_name" {
    type = string
    description = "Bastion subnet name"
    default = "bastionsubnet"  
}
# Bastion subnet address space
variable "bastion_subnet_address" {
    type = list(string)
    description = "bastion address space"
    default = ["10.0.100.0/24"]
}
