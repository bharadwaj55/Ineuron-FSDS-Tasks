
#Virtual network outputs
#Virtual network name
output "virtual_network_name" {
    description = "Virtual network name"
    value = azurerm_virtual_network.vnet.name
}
#Virtual network Id
output "virtual_network_Id" {
    description = "Virtual network Id"
    value = azurerm_virtual_network.vnet.id
}

#Subnet outputs
#Web Subnet name
output "web_subnet_name" {
    description = "Web subnet name"
    value = azurerm_subnet.websubnet.name
}
#Web Subnet Id
output "web_subnet_Id" {
    description = "Web subnet Id"
    value = azurerm_subnet.websubnet.id
}

#NSG outputs
#Web Subnet NSG name
output "web_subnet_nsg_name" {
    description = "Web subnet nsg name"
    value = azurerm_network_security_group.web_subnet_nsg.name
}

#Web Subnet NSG Id
output "web_subnet_nsg" {
    description = "Web subnet nsg Id"
    value = azurerm_network_security_group.web_subnet_nsg.id 
}