
## Public IP Outputs
## Public IP Address
output "web_linuxvm_publicip" {
    description = "Web linuxvm Public IP"
    value = azurerm_public_ip.web_linuxvm_publicip.ip_address
}


# Network Interface Outputs
## Network interface ID
output "web_linuxvm_network_interface_id" {
    description = "Web linuxvm network interface ID"
    value = azurerm_network_interface.web_linuxvm_nic.id
}

## Network interface Private IP address
output "web_linuxvm_network_interface_private_ip" {
    description = "Web linuxvm network interface private IP Address"
    value = [azurerm_network_interface.web_linuxvm_nic.private_ip_addresses]
}


# Linux VM Outputs
## Virtual Machine Public IP
output "web_linuxvm_public_ip_address" {
    description = "Web linuxvm Public IP Address"
    value = azurerm_linux_virtual_machine.web_linuxvm.public_ip_address
}

## Virtual Machine Private IP
output "web_linuxvm_private_ip_address" {
    description = "Web linuxvm Private IP Address"
    value = azurerm_linux_virtual_machine.web_linuxvm.private_ip_address
}

## Virtual Machine ID
output "web_linuxvm_id" {
    description = "Web linuxvm virtual machine ID"
    value = azurerm_linux_virtual_machine.web_linuxvm.id
}

## Virtual Machine 128-bit ID
output "web_linuxvm_virtual_machine_id" {
    description = "Web linuxvm virtual machine 128-ID"
    value = azurerm_linux_virtual_machine.web_linuxvm.virtual_machine_id
}