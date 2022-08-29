
# Resource-3 (Optional): Create Network Security Group and Associate to Linux VM Network Interface

# 1: Create Network Security Group (NSG)
resource "azurerm_network_security_group" "web_vmnic_nsg" {
  name                = "${azurerm_network_interface.web_linuxvm_nic.name}-nsg"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
}

# 2: Associate NSG & Linux VM NIC
resource "azurerm_network_interface_security_group_association" "web_vmnic_nsg_association" {
  depends_on = [azurerm_network_security_rule.web_vmnic_nsg_rule_inbound]
  network_interface_id      = azurerm_network_interface.web_linuxvm_nic.id
  network_security_group_id = azurerm_network_security_group.web_vmnic_nsg.id
}

# 3: Create NSG rules
locals {
  web_vm_nic_inbound_ports_map = {
    "100" : "8080",
    "110" : "80"
    "120" : "443",
    "130" : "22"
  }
}

# 4: NSG inbound rule for web tier subnets
resource "azurerm_network_security_rule" "web_vmnic_nsg_rule_inbound" {
  for_each = local.web_vm_nic_inbound_ports_map
  name                        = "Rule-Port-${each.value}"
  priority                    = each.key
  direction                   = "Inbound"
  access                      = "Allow"
  protocol                    = "Tcp"
  source_port_range           = "*"
  destination_port_range      = each.value
  source_address_prefix       = "*"
  destination_address_prefix  = "*"
  resource_group_name         = azurerm_resource_group.rg.name
  network_security_group_name = azurerm_network_security_group.web_vmnic_nsg.name
}


